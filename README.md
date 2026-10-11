# Employee Data Quality Checker

A Python-based project that checks employee CSV data for common data quality issues and generates a structured report.

## Features

- **Duplicate Employee IDs:** Identifies repeated employee IDs.
- **Missing Values:** Detects empty fields in employee records.
- **Invalid Salaries:** Flags negative or non-numeric salary values.
- **Quality Report:** Summarizes total records and detected data quality issues.

## Technologies Used

- Python
- CSV File Handling
- Dictionaries and Sets
- Functions and Loops
- Exception Handling

## Project Structure

```text
employee-data-quality-checker/
├── main.py
├── employees.csv
└── README.md
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

If your system uses `python3`, run `python3 main.py` instead.

## Sample Data

The included `employees.csv` file contains sample employee records for testing data quality checks, including duplicate IDs, missing values, and invalid salary entries.

## Future Improvements

- Add a graphical user interface.
- Support user-uploaded CSV files.
- Improve the report presentation and export options.

## Author

Kaushal Sharma

[GitHub](https://github.com/Kaushal-Sharma-04)
