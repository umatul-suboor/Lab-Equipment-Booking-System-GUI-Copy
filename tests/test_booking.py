from src.booking import create_booking, get_booking_records
from src.equipment import EQUIPMENT


def test_valid_booking():
    result = create_booking("1", 1, "2026-11-15")
    assert "Booking accepted" in result
    assert "Status: Pending" in result


def test_invalid_equipment():
    result = create_booking("99", 1, "2026-11-15")
    assert "Invalid equipment" in result


def test_insufficient_stock():
    result = create_booking("4", 10, "2026-11-15")
    assert "Invalid quantity or insufficient stock" in result


def test_invalid_date():
    result = create_booking("2", 1, "invalid-date")
    assert "Invalid date" in result


def test_stock_reduces_after_successful_booking():
    create_booking("2", 2, "2026-11-15")
    assert EQUIPMENT["2"]["available"] == 3


def test_stock_does_not_reduce_after_rejected_booking():
    create_booking("2", 8, "2026-11-15")
    assert EQUIPMENT["2"]["available"] == 5


def test_successful_booking_is_saved():
    create_booking("1", 1, "2026-11-15")
    assert len(get_booking_records()) == 1
    assert get_booking_records()[0]["status"] == "Pending"


def test_rejected_booking_is_not_saved():
    create_booking("99", 1, "2026-11-15")
    assert len(get_booking_records()) == 0
