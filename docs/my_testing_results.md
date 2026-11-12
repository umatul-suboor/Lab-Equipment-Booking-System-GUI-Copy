# My Application and Testing Notes

## Testing commands

Run the following commands from the project root:

```bash
python -m pytest -v
python -m pytest --cov=src --cov-report=term-missing
```

## Test areas

- Functional testing: equipment listing, valid booking, booking records and stock update.
- Boundary Value Analysis: -1, 0, 1, exact available stock and available stock + 1.
- Negative testing: invalid equipment ID, non-numeric quantity, zero/negative quantity, invalid date format and invalid calendar date.
- Unit testing: quantity validation, date validation and booking function.
- Integration testing: booking request through stock update and record creation.
- Regression testing: rerun the complete pytest suite after code changes.

## Actual results

Record the results produced on your own computer after running the commands above. Do not enter assumed results.
