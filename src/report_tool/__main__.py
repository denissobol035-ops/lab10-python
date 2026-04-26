import logging
import json
from pathlib import Path

from .cli import build_parser
from .parser import parse_numbers
from .analysis import analyze_numbers
from .formatter import build_report


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # logging setup
    logging.basicConfig(level=getattr(logging, args.log_level))
    logger = logging.getLogger(__name__)

    logger.info("Reading input file")
    text = Path(args.input).read_text()

    logger.info("Parsing numbers")
    numbers = parse_numbers(text)

    logger.info("Analyzing numbers")
    stats = analyze_numbers(numbers)

    logger.info("Generating output")

    if args.format == "text":
        result = build_report(stats)
    else:
        result = json.dumps(stats, indent=2)

    logger.info("Writing output file")
    Path(args.out).write_text(result)

    logger.info("Done")


if __name__ == "__main__":
    main()
