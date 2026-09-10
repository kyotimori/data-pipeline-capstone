import pytest

from common.exceptions import ValidationError
from common.models import Employee


def test_employee():
    assert Employee(345, 'Mary', 'IT', 3500).employee_id == 345


def test_employee_id():
    with pytest.raises(ValidationError, match="employee_id must be positive"):
        Employee(0, 'Mary', 'IT', 3500)
    with pytest.raises(ValidationError, match="employee_id must be positive"):
        Employee(None, 'Mary', 'IT', 3500)


def test_employee_first_name():
    with pytest.raises(ValidationError, match="first_name must not be empty"):
        Employee(345, None, 'IT', 3500)


def test_employee_salary():
    with pytest.raises(ValidationError, match="salary must be positive"):
        Employee(345, 'Mary', 'IT', -3500)


def test_optional_employee_fields():
    employee = Employee(1, 'Mary', None, None)
    
    assert employee.department is None
    assert employee.salary is None
    