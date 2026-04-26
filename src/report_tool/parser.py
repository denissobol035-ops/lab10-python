def parse_numbers(text: str) -> list[float]:
    import re

    parts = re.split(r"[,\s;]+", text.strip())
    return [float(p) for p in parts if p]
