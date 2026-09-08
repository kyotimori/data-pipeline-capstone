from pathlib import Path

import pandas as pd

from etl_utils.io import write_csv


class CsvStorage():
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def write(self, df: pd.DataFrame) -> None:
        write_csv(df, self.filepath)
