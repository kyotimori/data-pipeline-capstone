from pathlib import Path
import logging

import pandas as pd

from common.exceptions import SourceReadError
from etl_utils.io import read_csv


logger = logging.getLogger(__name__)


class CsvSource:
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def read(self) -> pd.DataFrame:
        logger.info(f"Reading file {self.filepath}")
        try:
            return read_csv(self.filepath)
        except Exception as exc:
            raise SourceReadError(f"Failed to read file {self.filepath}") from exc
