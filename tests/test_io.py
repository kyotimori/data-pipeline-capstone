from pathlib import Path

from etl_utils.io import read_csv


def test_read_csv():
    filepath = Path(__file__).parent / "data" / "employees_dirty.csv"
    df = read_csv(filepath)

    assert len(df) == 7
    assert "Employee ID" in df.columns
