from datetime import datetime


def validate_quantity(quantity, available_quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        return False
    return 0 < quantity <= available_quantity


def validate_date(booking_date):
    if not isinstance(booking_date, str) or not booking_date.strip():
        return False

    try:
        parsed_date = datetime.strptime(booking_date, "%Y-%m-%d")
        return parsed_date.strftime("%Y-%m-%d") == booking_date
    except ValueError:
        return False
