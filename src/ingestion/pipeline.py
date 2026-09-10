from common.ports import Source, Storage
from common.exceptions import ValidationError

from etl_utils.cleaning import (
    normalize_column_names,
    remove_duplicates
)
from etl_utils.validation import validate_required_columns


class Pipeline:
    def __init__(self, source: Source, storage: Storage):
        self.source = source
        self.storage = storage

    def run(self) -> None:
        df = self.source.read()

        df = normalize_column_names(df)
        df = remove_duplicates(df)

        required_columns = ['employee_id', 'first_name']
        if not validate_required_columns(df, required_columns):
            raise ValidationError(f"Required columns are missing: {set(required_columns) - set(df.columns)}")
        
        self.storage.write(df)
