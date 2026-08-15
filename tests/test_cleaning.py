import pandas as pd

from etl_utils.cleaning import (
    change_column_name,
    fill_missing_values,
    normalize_column_names,
    remove_duplicates,
)


def test_change_column_name():
    assert change_column_name("Employee ID") == "employee_id"
    assert change_column_name("$^Sala))ry *") == "salary"
    assert change_column_name(".    Sal!ary *  ") == "salary"
    assert change_column_name("Привет_") == "привет"
    assert change_column_name("user_id") == "user_id"


def test_normalize_column_names():
    data_1 = {
        "имя": ["Анна", "Иван", "Ольга"],
        "возраст": [25, 30, 22],
        "город": ["Москва", "Санкт-Петербург", "Казань"],
    }
    data_2 = {
        "_имя.    ": ["Анна", "Иван", "Ольга"],
        "Возр&%аст": [25, 30, 22],
        "ГОРОД": ["Москва", "Санкт-Петербург", "Казань"],
    }
    df_1 = pd.DataFrame(data_1)
    df_2 = normalize_column_names(pd.DataFrame(data_2))

    assert df_1.equals(df_2)


def test_remove_duplicates():
    # testcase 1
    data_1 = {
        "имя": ["Анна", "Иван", "Ольга"],
        "возраст": [25, 30, 22],
        "город": ["Москва", "Санкт-Петербург", "Казань"],
    }
    data_2 = {
        "имя": ["Анна", "Иван", "Иван", "Ольга"],
        "возраст": [25, 30, 30, 22],
        "город": ["Москва", "Санкт-Петербург", "Санкт-Петербург", "Казань"],
    }
    df_1 = pd.DataFrame(data_1)
    df_2 = pd.DataFrame(data_2)
    assert len(df_1) == len(remove_duplicates(df_2))

    # testcase 2
    data_1 = {"имя": ["Анна"], "возраст": [25], "город": ["Москва"]}
    data_2 = {
        "имя": ["Анна", "Анна", "Анна"],
        "возраст": [25, 25, 25],
        "город": ["Москва", "Москва", "Москва"],
    }
    df_1 = pd.DataFrame(data_1)
    df_2 = pd.DataFrame(data_2)
    assert len(df_1) == len(remove_duplicates(df_2))

    # testcase 3
    data_1 = {
        "имя": ["Анна", "Иван", "Ольга"],
        "возраст": [25, 30, 22],
        "город": ["Москва", "Санкт-Петербург", "Казань"],
    }
    df_1 = pd.DataFrame(data_1)
    assert len(df_1) == len(remove_duplicates(df_1))


def test_fill_missing_values():
    # testcase 1
    data_1 = {
        "имя": ["Анна", "Иван", "NULL", "Ольга"],
        "возраст": ["NULL", 25, 30, 22],
        "город": ["Москва", "NULL", "Санкт-Петербург", "Казань"],
    }
    data_2 = {
        "имя": ["Анна", "Иван", None, "Ольга"],
        "возраст": [None, 25, 30, 22],
        "город": ["Москва", None, "Санкт-Петербург", "Казань"],
    }
    df_1 = pd.DataFrame(data_1)
    df_2 = pd.DataFrame(data_2)
    assert df_1.equals(fill_missing_values(df_2))

    # testcase 2
    data_1 = {
        "имя": ["Анна", "Иван", 0.0, "Ольга"],
        "возраст": [0.0, 25, 30, 22],
        "город": ["Москва", 0.0, "Санкт-Петербург", "Казань"],
    }
    data_2 = {
        "имя": ["Анна", "Иван", None, "Ольга"],
        "возраст": [None, 25, 30, 22],
        "город": ["Москва", None, "Санкт-Петербург", "Казань"],
    }
    df_1 = pd.DataFrame(data_1)
    df_2 = pd.DataFrame(data_2)
    assert df_1.equals(fill_missing_values(df_2, 0))

    # testcase 3
    data_1 = {
        "имя": ["Анна", "Иван", "", "Ольга"],
        "возраст": ["", 25, 30, 22],
        "город": ["Москва", "", "Санкт-Петербург", "Казань"],
    }
    data_2 = {
        "имя": ["Анна", "Иван", None, "Ольга"],
        "возраст": [None, 25, 30, 22],
        "город": ["Москва", None, "Санкт-Петербург", "Казань"],
    }
    df_1 = pd.DataFrame(data_1)
    df_2 = pd.DataFrame(data_2)
    assert df_1.equals(fill_missing_values(df_2, ""))
