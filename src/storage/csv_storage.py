from pathlib import Path
import logging

import pandas as pd

from common.exceptions import StorageWriteError
from etl_utils.io import write_csv


logger = logging.getLogger(__name__)

class CsvStorage():
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def write(self, df: pd.DataFrame) -> None:
        logger.info(f"Writing into file {self.filepath}")
        try:
            write_csv(df, self.filepath)
        except Exception as exc:
            raise StorageWriteError(f"Failed to write to file {self.filepath}") from exc
