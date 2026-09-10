class AppError(Exception):
    """Базовая ошибка приложения"""


class ConfigurationError(AppError):
    """Ошибка конфигурации приложения."""


class SourceReadError(AppError):
    """Ошибка чтения источника"""


class StorageWriteError(AppError):
    """Ошибка записи"""   


class ValidationError(AppError):
    """Ошибка валидации""" 