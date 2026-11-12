from src.equipment import EQUIPMENT, display_equipment


def test_equipment_ids_exist():
    assert set(EQUIPMENT.keys()) == {"1", "2", "3", "4"}


def test_equipment_have_non_negative_stock():
    assert all(item["available"] >= 0 for item in EQUIPMENT.values())


def test_display_equipment(capsys):
    display_equipment()
    output = capsys.readouterr().out
    assert "Projector" in output
    assert "Laptop" in output
    assert "HDMI Cable" in output
    assert "Microphone" in output
