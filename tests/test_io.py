import pytest
from etl_utils.io import read_csv


def test_read_csv():
    filepath = '/Users/dariaprovorova/Documents/DE Course/employes_dirty.csv'
    df = read_csv(filepath)

    assert len(df) == 7
    assert 'Employee ID' in df.columns