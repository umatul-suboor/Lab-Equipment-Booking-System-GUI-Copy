from src.booking import create_booking, get_booking_records
from src.equipment import EQUIPMENT


def test_complete_booking_flow_updates_stock_and_record():
    result = create_booking("2", 2, "2026-11-15")

    assert "Booking accepted" in result
    assert EQUIPMENT["2"]["available"] == 3

    records = get_booking_records()
    assert len(records) == 1
    assert records[0]["equipment"] == "Laptop"
    assert records[0]["quantity"] == 2
    assert records[0]["status"] == "Pending"
