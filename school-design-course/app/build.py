#!/usr/bin/env python3
"""Inline app/data/*.json into template.html -> founding-school.html."""
import json
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"


def load(name, key):
    path = DATA / name
    if not path.exists():
        print(f"missing {name}")
        return []
    return json.loads(path.read_text())[key]


def main():
    modules = []
    for name in ("modules-a.json", "modules-b.json"):
        modules += load(name, "modules")
    modules.sort(key=lambda m: int(str(m["id"]).lstrip("m")))
    for m in modules:
        m.setdefault("num", int(str(m["id"]).lstrip("m")))

    bundle = {
        "modules": modules,
        "cards": load("flashcards.json", "cards"),
        "cases": load("cases.json", "cases"),
        "tensions": load("tensions.json", "tensions"),
        "brief": load("brief.json", "sections"),
        "diagnostic": load("diagnostic.json", "items"),
        "model": json.loads((DATA / "model.json").read_text()) if (DATA / "model.json").exists() else {"bands": []},
    }
    payload = json.dumps(bundle, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (HERE / "template.html").read_text().replace("/*__DATA__*/", payload)
    out = HERE / "founding-school.html"
    out.write_text(html)
    print(f"wrote {out} ({len(html) // 1024} KB): " + ", ".join(f"{k}={len(v) if isinstance(v, list) else len(v.get('bands', []))}" for k, v in bundle.items()))


if __name__ == "__main__":
    main()
