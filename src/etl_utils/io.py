from pathlib import Path

import pandas as pd


def read_csv(filepath: str | Path) -> pd.DataFrame:
    """Load CSV file to DataFrame"""
    return pd.read_csv(filepath)


def write_csv(df: pd.DataFrame, filepath: str | Path) -> None:
    """Write DataFrame into CSV file"""
    df.to_csv(filepath, index=False)
