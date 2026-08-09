import pandas as pd
from typing import Any


def validate_required_columns(df: pd.DataFrame, required_columns: list[str]) -> bool:
    """Проверяет наличие обязательных колонок."""
    return set(required_columns).issubset(set(df.columns))


def validate_not_empty_columns(df: pd.DataFrame, not_empty_columns: list[str]) -> bool:
    """Проверяет заполнение колонок, которые не должны быть полностью пустыми"""
    empty_columns = [col for col in df.columns if df[col].isna().all()]
    return set(empty_columns).isdisjoint(set(not_empty_columns))


def validate_salary(salary: Any) -> bool:
    """Проверяет значения в столбце Salary. Условие: >0"""
    return salary > 0