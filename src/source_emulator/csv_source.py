from pathlib import Path

import pandas as pd

from common.exceptions import SourceReadError
from etl_utils.io import read_csv


class CsvSource:
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def read(self) -> pd.DataFrame:
        try:
            return read_csv(self.filepath)
        except Exception as exc:
            raise SourceReadError(f"Failed to read file {self.filepath}") from exc
