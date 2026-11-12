from src.main import run_cli


def test_cli_can_exit(monkeypatch, capsys):
    answers = iter(["4"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    run_cli()

    output = capsys.readouterr().out
    assert "LAB EQUIPMENT BOOKING SYSTEM" in output
    assert "Thank you for using the system." in output


def test_cli_can_display_equipment(monkeypatch, capsys):
    answers = iter(["1", "4"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    run_cli()

    output = capsys.readouterr().out
    assert "Projector" in output
    assert "Laptop" in output


def test_cli_rejects_non_numeric_quantity(monkeypatch, capsys):
    answers = iter(["2", "1", "abc", "4"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))

    run_cli()

    output = capsys.readouterr().out
    assert "Quantity must be a whole number." in output
