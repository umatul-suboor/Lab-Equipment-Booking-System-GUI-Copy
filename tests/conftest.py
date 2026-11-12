import pytest
from src.equipment import reset_equipment
from src.booking import reset_bookings


@pytest.fixture(autouse=True)
def reset_project_data():
    reset_equipment()
    reset_bookings()
    yield
    reset_equipment()
    reset_bookings()
