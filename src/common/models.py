from dataclasses import dataclass

from common.exceptions import ValidationError


@dataclass(frozen=True)
class Employee:
    employee_id: int
    first_name: str
    department: str | None
    salary: float | None

    def __post_init__(self) -> None:
        if not isinstance(self.employee_id, int) or self.employee_id <= 0:
            raise ValidationError('employee_id must be positive')
        if not isinstance(self.first_name, str) or not self.first_name.strip():
            raise ValidationError('first_name must not be empty')
        if self.salary is not None and self.salary <= 0:
            raise ValidationError('salary must be positive')
