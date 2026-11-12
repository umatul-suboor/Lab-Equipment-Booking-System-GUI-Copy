from src.equipment import EQUIPMENT
from src.validation import validate_quantity, validate_date

BOOKING_RECORDS = []


def create_booking(equipment_id, quantity, booking_date):
    if equipment_id not in EQUIPMENT:
        return "Booking rejected: Invalid equipment."

    available = EQUIPMENT[equipment_id]["available"]

    if not validate_quantity(quantity, available):
        return "Booking rejected: Invalid quantity or insufficient stock."

    if not validate_date(booking_date):
        return "Booking rejected: Invalid date."

    item = EQUIPMENT[equipment_id]
    item["available"] -= quantity

    record = {
        "booking_id": len(BOOKING_RECORDS) + 1,
        "equipment_id": equipment_id,
        "equipment": item["name"],
        "quantity": quantity,
        "date": booking_date,
        "status": "Pending",
    }
    BOOKING_RECORDS.append(record)

    return (
        "Booking accepted.\n"
        f"Equipment: {item['name']}\n"
        f"Quantity: {quantity}\n"
        f"Date: {booking_date}\n"
        "Status: Pending"
    )


def get_booking_records():
    return BOOKING_RECORDS


def reset_bookings():
    BOOKING_RECORDS.clear()
