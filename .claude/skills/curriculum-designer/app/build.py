#!/usr/bin/env python3
"""Build a course app: inline <course>/app/data/*.json + course.json into template.html.

Usage: build.py <course-dir> [--template PATH] [--out PATH]
Writes <course-dir>/app/<slug>.html by default.
"""
import argparse
import html
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def load(data_dir, name, key):
    path = data_dir / name
    if not path.exists():
        print(f"  missing {name}", file=sys.stderr)
        return []
    return json.loads(path.read_text())[key]


def build(course_dir: Path, template: Path, out: Path | None) -> Path:
    course = json.loads((course_dir / "course.json").read_text())
    data = course_dir / "app" / "data"
    modules = []
    for f in sorted(data.glob("modules*.json")):
        modules += json.loads(f.read_text())["modules"]
    modules.sort(key=lambda m: int(str(m["id"]).lstrip("m")))
    for m in modules:
        m.setdefault("num", int(str(m["id"]).lstrip("m")))
    model_path = data / "model.json"
    bundle = {
        "course": course,
        "modules": modules,
        "cards": load(data, "flashcards.json", "cards"),
        "cases": load(data, "cases.json", "cases"),
        "tensions": load(data, "tensions.json", "tensions"),
        "brief": load(data, "brief.json", "sections"),
        "diagnostic": load(data, "diagnostic.json", "items"),
        "model": json.loads(model_path.read_text()) if model_path.exists() else {"bands": []},
    }
    payload = json.dumps(bundle, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = (template.read_text()
            .replace("{{TITLE}}", html.escape(course.get("title", "Course")))
            .replace("{{DESCRIPTION}}", html.escape(course.get("description", "")))
            .replace("/*__DATA__*/", payload))
    out = out or course_dir / "app" / f"{course.get('slug', 'course')}.html"
    out.write_text(page)
    counts = ", ".join(f"{k}={len(v) if isinstance(v, list) else len(v.get('bands', []))}"
                       for k, v in bundle.items() if k != "course")
    print(f"wrote {out} ({len(page) // 1024} KB): {counts}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("course_dir", type=Path)
    ap.add_argument("--template", type=Path, default=HERE / "template.html")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    build(a.course_dir.resolve(), a.template, a.out)
