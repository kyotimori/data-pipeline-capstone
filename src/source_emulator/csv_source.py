from pathlib import Path

import pandas as pd

from etl_utils.io import read_csv


class CsvSource:
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def read(self) -> pd.DataFrame:
        return read_csv(self.filepath)
