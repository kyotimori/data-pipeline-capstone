from pathlib import Path

import pandas as pd

from common.exceptions import StorageWriteError
from etl_utils.io import write_csv


class CsvStorage():
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def write(self, df: pd.DataFrame) -> None:
        try:
            write_csv(df, self.filepath)
        except Exception as exc:
            raise StorageWriteError(f"Failed to write to file {self.filepath}") from exc
