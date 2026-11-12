from src.booking import create_booking, get_booking_records


def test_booking_records_start_empty():
    assert get_booking_records() == []


def test_multiple_booking_records():
    create_booking("1", 1, "2026-11-15")
    create_booking("2", 1, "2026-11-16")
    records = get_booking_records()

    assert len(records) == 2
    assert records[0]["booking_id"] == 1
    assert records[1]["booking_id"] == 2
