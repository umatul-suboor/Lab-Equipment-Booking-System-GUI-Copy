from src.validation import validate_quantity, validate_date


def test_valid_quantity():
    assert validate_quantity(2, 5) is True


def test_zero_quantity():
    assert validate_quantity(0, 5) is False


def test_negative_quantity():
    assert validate_quantity(-1, 5) is False


def test_quantity_exceeds_stock():
    assert validate_quantity(6, 5) is False


def test_maximum_available_quantity():
    assert validate_quantity(5, 5) is True


def test_minimum_valid_quantity():
    assert validate_quantity(1, 5) is True


def test_non_numeric_quantity():
    assert validate_quantity("abc", 5) is False


def test_empty_date():
    assert validate_date("") is False


def test_valid_date():
    assert validate_date("2026-11-15") is True


def test_wrong_date_format():
    assert validate_date("15-11-2026") is False


def test_invalid_calendar_date():
    assert validate_date("2026-02-30") is False
