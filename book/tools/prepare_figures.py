"""Copy referenced original figures into the publishing asset tree."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "Sections"
TARGET = ROOT / "book" / "figures" / "original"


def main() -> None:
    TARGET.mkdir(parents=True, exist_ok=True)
    copied = []
    for tex in SOURCE.rglob("*.tex"):
        text = tex.read_text(encoding="utf-8")
        for rel in re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", text):
            source = ROOT / rel
            rel = Path(*Path(rel).parts[1:]) if Path(rel).parts and Path(rel).parts[0].lower() == "Images".lower() else Path(rel)
            rel = Path(*[part.replace(" ", "") for part in rel.parts])
            target = TARGET / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            copied.append(rel)
    print(f"Prepared {len(set(copied))} original Differential Calculus figures in {TARGET}")


if __name__ == "__main__":
    main()
