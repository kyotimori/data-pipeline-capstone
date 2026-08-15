from pathlib import Path

import pandas as pd

from etl_utils.io import read_csv, write_csv


def test_read_csv():
    filepath = Path(__file__).parent / "data" / "employees_dirty.csv"
    df = read_csv(filepath)

    assert len(df) == 7
    assert "Employee ID" in df.columns


def test_write_csv(tmp_path):
    data = {
        "имя": ["Анна", "Иван", "Ольга"],
        "возраст": [25, 30, 22],
        "город": ["Москва", "Санкт-Петербург", "Казань"],
    }
    df = pd.DataFrame(data)
    filepath = tmp_path / "test_write_csv.csv"
    write_csv(df, filepath)

    assert df.equals(read_csv(filepath))
