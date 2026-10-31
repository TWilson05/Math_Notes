"""Migrate every remaining top-level course into the established MyST tree.

The converter is deliberately structural. It keeps mathematical source text,
records source paths, and reports constructs that need visual/manual review.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from convert_differential import convert  # noqa: E402

SECTIONS = ROOT / "Sections"
BOOK = ROOT / "book"
SKIP = {"Differential_Calculus"}


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def title(path: Path, fallback: str) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"\\section\{([^}]*)\}", text) or re.search(r"\\subsection\{([^}]*)\}", text)
    return match.group(1) if match else fallback.replace("_", " ")


def imports(root: Path) -> list[str]:
    text = root.read_text(encoding="utf-8")
    found = re.findall(r"\\subimport\*?\{[^}]*\}\{([^}]+)\}", text)
    return [Path(x).stem for x in found]


def main() -> None:
    courses = []
    coverage = {}
    for root in sorted(SECTIONS.glob("*.tex")):
        name = root.stem
        if name in SKIP:
            continue
        target = BOOK / slug(name)
        target.mkdir(parents=True, exist_ok=True)
        child_dir = SECTIONS / name
        if child_dir.is_dir():
            files = {p.stem: p for p in child_dir.glob("*.tex")}
            order = imports(root)
            ordered = [files[key] for key in order if key in files]
            ordered += [files[key] for key in sorted(files) if key not in order]
        else:
            files = {root.stem: root}
            ordered = [root]
        for source in ordered:
            (target / f"{source.stem}.md").write_text(convert(source), encoding="utf-8")
        chapter_title = title(root, name)
        entries = [p.stem for p in ordered]
        index_lines = [f"# {chapter_title}", "", f"This chapter preserves the source hierarchy from `{root.relative_to(ROOT).as_posix()}`. Each page records its original TeX source for traceability.", "", "```{toctree}", ":maxdepth: 2", "", *entries, "```", ""]
        (target / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
        special = []
        for source in ordered:
            text = source.read_text(encoding="utf-8")
            for env in sorted(set(re.findall(r"\\begin\{([^}]+)\}", text))):
                if env not in {"align*", "flalign*", "itemize", "enumerate", "description", "tabular", "center", "small", "multicols"}:
                    special.append(f"{source.name}: environment {env}")
            if r"\polylongdiv" in text:
                special.append(f"{source.name}: polylongdiv requires manual review")
        coverage[name] = {
            "title": chapter_title,
            "original_files": [p.relative_to(ROOT).as_posix() for p in ordered],
            "new_files": [(target / f"{p.stem}.md").relative_to(ROOT).as_posix() for p in ordered],
            "special_constructs": special,
            "status": "migrated-structural-review",
        }
        courses.append((name, chapter_title, slug(name)))
    # Preserve Differential Calculus as the first completed chapter.
    index = BOOK / "index.md"
    lines = ["# Mathematics Notes", "", "This is the unified online mathematics textbook. Original LaTeX remains under `Sections/`; migrated MyST content is under `book/`.", "", "```{toctree}", ":maxdepth: 2", ":numbered:", "", "differential-calculus/index", *[f"{s}/index" for _, _, s in courses], "figures/workflow-example", "```", ""]
    index.write_text("\n".join(lines), encoding="utf-8")
    (BOOK / "_build").mkdir(exist_ok=True)
    (BOOK / "_build" / "migration-coverage.json").write_text(json.dumps(coverage, indent=2) + "\n", encoding="utf-8")
    print(f"Migrated {len(courses)} remaining courses and updated {index}")


if __name__ == "__main__":
    main()
