from dataclasses import dataclass
from .exceptions import ConfigurationError
from pathlib import Path
import os


@dataclass
class AppConfig:
    input_path: Path
    output_path: Path
    log_level: str = "INFO"

    def __post_init__(self):
        if not os.path.exists(self.input_path):
            raise ConfigurationError('Input path does not exists')
        if not os.path.exists(self.output_path):
            raise ConfigurationError('Output path does not exists')
        if self.log_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            raise ConfigurationError('Incorrect log level')


@dataclass
class DatabaseConfig:
    host: str
    port: int
    database: str
    user: str
    password: str
