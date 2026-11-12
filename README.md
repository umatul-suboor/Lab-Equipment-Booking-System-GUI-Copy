# Lab Equipment Booking and Management System

A beginner-friendly Python project that provides both a desktop GUI and a command-line interface.

## Features

- Dashboard with equipment and booking summaries
- Equipment listing and available stock
- Equipment booking form
- Quantity and date validation
- Booking records with Pending status
- Stock is reduced only after a successful booking
- Temporary in-memory records (no database)
- Automated tests using pytest

## Requirements

- Python 3.10 or later
- Tkinter (normally included with standard Python on Windows)
- pytest and pytest-cov for testing

## Setup

Open this folder in VS Code and open the terminal.

```bash
python -m pip install -r requirements.txt
```

## Run desktop GUI

```bash
python -m src.main
```

The desktop dashboard opens in a separate window.

## Run CLI mode

```bash
python -m src.main --cli
```

## Run automated tests

```bash
python -m pytest -v
```

## Run coverage

```bash
python -m pytest --cov=src --cov-report=term-missing
```

## Notes

- Booking records and stock changes are stored in memory only.
- Data resets when the application closes or the program restarts.
- The GUI uses Python Tkinter and does not require a web browser or database.

## Coverage note

The Tkinter screen is a graphical interface and is checked manually on Windows.
The automated coverage report focuses on the testable application and CLI logic;
the GUI presentation file is excluded from line coverage.
