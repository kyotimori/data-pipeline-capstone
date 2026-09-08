from dataclasses import dataclass


@dataclass(frozen=True)
class Employee:
    employee_id: int
    first_name: str
    department: str | None
    salary: float | None

    def __post_init__(self):
        if not isinstance(self.employee_id, int) or self.employee_id <= 0:
            raise ValueError('employee_id must be positive')
        if not isinstance(self.first_name, str) or not self.first_name.strip():
            raise ValueError('first_name must not be empty')
        if self.salary is not None and self.salary <= 0:
            raise ValueError('salary must be positive')
