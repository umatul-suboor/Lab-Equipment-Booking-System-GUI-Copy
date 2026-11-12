from src.equipment import EQUIPMENT


def test_project_has_sample_equipment():
    assert len(EQUIPMENT) == 4
    assert EQUIPMENT["1"]["name"] == "Projector"
