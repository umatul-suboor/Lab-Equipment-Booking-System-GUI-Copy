# BVA and Negative Testing Report

## Lab Equipment Booking and Management System

### 1. Boundary Value Analysis (BVA)

Boundary Value Analysis checks values at, below, and above the valid quantity boundaries.

**Test data:** Laptop stock = 5

| Test ID | Test scenario | Input | Expected result | Actual result | Automated test function | Status |
|---|---|---:|---|---|---|---|
| BVA-01 | Quantity below minimum | -1 | Booking rejected | Quantity validation rejected the value | `test_negative_quantity()` | Pass |
| BVA-02 | Quantity at zero boundary | 0 | Booking rejected | Quantity validation rejected the value | `test_zero_quantity()` | Pass |
| BVA-03 | Minimum valid quantity | 1 | Booking accepted | Quantity validation accepted the value | `test_minimum_valid_quantity()` | Pass |
| BVA-04 | Maximum available quantity | 5 | Booking accepted | Quantity validation accepted the value | `test_maximum_available_quantity()` | Pass |
| BVA-05 | Quantity above available stock | 6 | Booking rejected | Quantity validation rejected the value | `test_quantity_exceeds_stock()` | Pass |

### 2. Negative Testing

Negative testing checks how the system handles invalid inputs and requests.

| Test ID | Test scenario | Input | Expected result | Actual result | Automated test function | Status |
|---|---|---|---|---|---|---|
| NEG-01 | Invalid equipment ID | `99` | Show invalid equipment message and reject booking | Booking returned an invalid equipment message | `test_invalid_equipment()` | Pass |
| NEG-02 | Non-numeric quantity | `abc` | Reject quantity | Quantity validation rejected non-numeric input | `test_non_numeric_quantity()` and `test_cli_rejects_non_numeric_quantity()` | Pass |
| NEG-03 | Zero quantity | `0` | Reject booking | Quantity validation rejected zero | `test_zero_quantity()` | Pass |
| NEG-04 | Negative quantity | `-1` | Reject booking | Quantity validation rejected the negative value | `test_negative_quantity()` | Pass |
| NEG-05 | Quantity greater than stock | `8` when stock is `5` | Reject booking and do not reduce stock | Booking was rejected and stock remained unchanged | `test_stock_does_not_reduce_after_rejected_booking()` | Pass |
| NEG-06 | Empty booking date | Empty string | Reject date | Date validation rejected the empty date | `test_empty_date()` | Pass |
| NEG-07 | Incorrect date format | `15-11-2026` | Reject date | Date validation rejected the incorrect format | `test_wrong_date_format()` | Pass |
| NEG-08 | Invalid calendar date | `2026-02-30` | Reject date | Date validation rejected the invalid calendar date | `test_invalid_calendar_date()` | Pass |
| NEG-09 | Invalid date text | `invalid-date` | Reject booking | Booking returned an invalid date message | `test_invalid_date()` | Pass |

### 3. Test Execution Summary

| Testing type | Test cases | Passed | Failed |
|---|---:|---:|---:|
| Boundary Value Analysis | 5 | 5 | 0 |
| Negative Testing | 9 | 9 | 0 |
| **Total documented cases** | **14** | **14** | **0** |

### 4. Automated Test Suite

The project contains 29 automated test functions across 7 test files.

| Test file | Number of test functions |
|---|---:|
| `test_equipment.py` | 3 |
| `test_booking.py` | 8 |
| `test_booking_records.py` | 2 |
| `test_integration.py` | 1 |
| `test_cli.py` | 3 |
| `test_validation.py` | 11 |
| `test_smoke.py` | 1 |
| **Total** | **29** |

**Reported test run:** 29 passed, 0 failed.

**Note:** The BVA and Negative Testing tables document 14 selected test scenarios. Some scenarios use the same automated test function in both categories. The full automated test suite contains 29 test functions. Run `python -m pytest tests -v` in the project folder to verify the current test results.
