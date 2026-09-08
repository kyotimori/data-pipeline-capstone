from pathlib import Path
import pytest
import pandas as pd

from ingestion.pipeline import Pipeline
from source_emulator.csv_source import CsvSource
from storage.csv_storage import CsvStorage


def test_pipeline(tmp_path):
    source_filepath = Path(__file__).parent / "data" / "employees_dirty.csv"
    storage_filepath = tmp_path / "test_write_csv.csv"
    source = CsvSource(source_filepath)
    storage = CsvStorage(storage_filepath)

    pipeline = Pipeline(source, storage)
    pipeline.run()

    assert storage_filepath.exists
    assert not pd.read_csv(storage_filepath).empty


def test_pipeline_wo_required_columns(tmp_path):
    source_filepath = Path(__file__).parent / "data" / "employees_dirty_wo_required_columns.csv"
    storage_filepath = tmp_path / "test_write_csv.csv"
    source = CsvSource(source_filepath)
    storage = CsvStorage(storage_filepath)

    pipeline = Pipeline(source, storage)

    with pytest.raises(ValueError, match="Required columns are missing"):
        pipeline.run()
