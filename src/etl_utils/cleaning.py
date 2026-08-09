import pandas as pd
import re
from typing import Any


def change_column_name(column_name: str) -> str:
    """Преобразование строки к универсальному виду"""
    new_column_name = column_name.replace('_', ' ')
    new_column_name = re.sub(r'[^a-zA-Zа-яА-ЯёЁ ]', '', new_column_name)
    new_column_name = new_column_name.lower().strip().replace(' ', '_')
    
    return new_column_name

def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Преобразование названий колонок к универсальному виду"""
    new_columns = []
    new_columns = [change_column_name(column_name) for column_name in df.columns]
    
    new_df = df.copy()
    new_df.columns = new_columns

    return new_df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Удаление полых дубликатов строк"""
    return df.drop_duplicates()

def fill_missing_values(df: pd.DataFrame, none_value: Any = 'NULL') -> pd.DataFrame:
    """Заполнение None значений"""
    return df.fillna(none_value)