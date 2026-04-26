from pathlib import Path


def save_report(report: str, filename: str) -> Path:
    path = Path(f"{filename}.txt")
    path.write_text(report)
    return path


def read_back(path: str) -> str:
    return Path(path).read_text()
