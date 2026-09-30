#!/usr/bin/env python3
"""Build founding-school.html with the shared curriculum-designer template."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.exit(subprocess.call([sys.executable, ROOT / ".claude/skills/curriculum-designer/app/build.py", ROOT / "school-design-course", "--out", Path(__file__).parent / "founding-school.html"]))
