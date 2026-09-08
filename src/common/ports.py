from typing import Protocol

import pandas as pd


class Source(Protocol):
    def read(self) -> pd.DataFrame:
        ...


class Storage(Protocol):
    def write(self, df: pd.DataFrame) -> None:
        ...