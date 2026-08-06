import pandas as pd
from pathlib import Path
from typing import Union


def read_csv(filepath: Union[str, Path]) -> pd.DataFrame:
    """Load CSV file to DataFrame"""
    return pd.read_csv(filepath)

def write_csv(df: pd.DataFrame, filepath: Union[str, Path]) -> None:
    """Write DataFrame into CSV file"""
    df.to_csv(filepath, index=False)