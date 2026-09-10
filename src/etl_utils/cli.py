import argparse
from pathlib import Path

from common.config import AppConfig
from common.exceptions import AppError
from common.logging import setup_logging
from ingestion.pipeline import Pipeline
from source_emulator.csv_source import CsvSource
from storage.csv_storage import CsvStorage


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run ETL pipeline"
    )

    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--log-level", 
                        default="INFO", 
                        choices=["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"])
    
    return parser


def main() -> int:
    args = create_parser().parse_args()

    try:
        app_config = AppConfig(args.input, 
                               args.output, 
                               args.log_level,
        )
        
        setup_logging(app_config.log_level)

        source = CsvSource(app_config.input_path)
        storage = CsvStorage(app_config.output_path)

        pipeline = Pipeline(source, storage)
        pipeline.run()

        return 0
    except AppError as exc:
        print(f"Application error: {exc}")
        return 1
    

if __name__ == "__main__":
    raise SystemExit(main())
