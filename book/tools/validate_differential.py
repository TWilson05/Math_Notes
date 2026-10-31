"""Structural parity checks for the complete Differential Calculus migration."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "Sections" / "Differential_Calculus"
OUT = ROOT / "book" / "differential-calculus"


def main() -> None:
    report = {"files": {}, "figures": 0, "errors": []}
    for source in sorted(SRC.glob("*.tex")):
        target = OUT / f"{source.stem}.md"
        original = source.read_text(encoding="utf-8")
        converted = target.read_text(encoding="utf-8")
        assert f"Sections/Differential_Calculus/{source.name}" in converted
        equations = len(re.findall(r"\\begin\{(?:align\*|flalign\*)\}", original))
        aligned = converted.count(r"\begin{aligned}")
        graphics = re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", original)
        for graphic in graphics:
            rel = Path(*Path(graphic).parts[1:]) if Path(graphic).parts and Path(graphic).parts[0].lower() == "images" else Path(graphic)
            expected = rel.as_posix().replace(" ", "")
            assert f"../figures/original/{expected}" in converted, f"Missing figure reference {graphic} in {source.name}"
            assert (ROOT / graphic).exists(), f"Missing original figure {graphic}"
        assert equations == aligned, f"Equation block count changed in {source.name}: {equations} != {aligned}"
        report["files"][source.name] = {"source_lines": len(original.splitlines()), "migrated_lines": len(converted.splitlines()), "equation_blocks": equations, "figures": len(graphics)}
        report["figures"] += len(graphics)
    assert len(report["files"]) == 6
    (ROOT / "book" / "_build").mkdir(exist_ok=True)
    (ROOT / "book" / "_build" / "differential-parity.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
