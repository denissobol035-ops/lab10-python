import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Report Tool CLI")

    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--out", required=True, help="Output file path")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        required=True,
        help="Output format",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Logging level",
    )

    return parser
