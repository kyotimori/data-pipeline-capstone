import numpy as np
import pandas as pd

from etl_utils.validation import (
    validate_not_empty_columns,
    validate_required_columns,
    validate_salary,
)


def test_validate_required_columns():
    required_columns_1 = ["employee_id", "first_name", "department", "salary"]
    data_1 = {
        "employee_id": [1, 2, 3, 4, 5, 6, 7],
        "first_name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Eve", " Frank "],
        "department": ["sales", "IT", "", "finance", "Sales", "Sales", "HR"],
        "salary": [3500, 4200, 3900, -100, np.nan, np.nan, 5100],
    }
    df_1 = pd.DataFrame(data_1)
    assert validate_required_columns(df_1, required_columns_1) is True

    required_columns_2 = ["employee_id", "first_name", "department", "salary"]
    data_2 = {
        "employee_id": [1, 2, 3, 4, 5, 6, 7],
        "first_name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Eve", " Frank "],
        "department": ["sales", "IT", "", "finance", "Sales", "Sales", "HR"],
    }
    df_2 = pd.DataFrame(data_2)
    assert validate_required_columns(df_2, required_columns_2) is False


def test_validate_not_empty_columns():
    not_empty_columns_1 = ["employee_id", "first_name"]
    data_1 = {
        "employee_id": [1, 2, 3, 4, 5, 6, 7],
        "first_name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Eve", " Frank "],
        "department": ["sales", "IT", "", "finance", "Sales", "Sales", "HR"],
        "salary": [3500, 4200, 3900, -100, np.nan, np.nan, 5100],
    }
    df_1 = pd.DataFrame(data_1)
    assert validate_not_empty_columns(df_1, not_empty_columns_1) is True

    not_empty_columns_2 = ["employee_id", "first_name"]
    data_2 = {
        "employee_id": [
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
            np.nan,
        ],
        "first_name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Eve", " Frank "],
        "department": ["sales", "IT", "", "finance", "Sales", "Sales", "HR"],
        "salary": [3500, 4200, 3900, -100, np.nan, np.nan, 5100],
    }
    df_2 = pd.DataFrame(data_2)
    assert validate_not_empty_columns(df_2, not_empty_columns_2) is False


def test_validate_salary():
    assert validate_salary(3500) is True
    assert validate_salary(-3500) is False
    assert validate_salary(0) is False
    assert validate_salary(np.nan) is False
