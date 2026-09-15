# Student Result Management System

A desktop-based Student Result Management System developed using Python and Tkinter.

## Objective

The objective of this project is to provide a simple and user-friendly system for storing, calculating, searching, and displaying student results.

## Features

- Add student details and marks
- Automatic calculation of total marks
- Automatic percentage calculation
- Automatic Pass/Fail result
- Search student result using Roll Number
- Display all student results
- Dashboard with student statistics
- Prevent duplicate Roll Numbers
- Store records in an Excel file

## Subjects

- Python
- Computer Networks
- DBMS
- Mathematics
- Web Technology

## Technologies Used

- Python
- Tkinter
- OpenPyXL
- Microsoft Excel

## How to Run

1. Install Python.
2. Install OpenPyXL:
   `python -m pip install openpyxl`
3. Open the project folder in VS Code.
4. Run:

   `python main.py`

## Project Files

- `main.py` – Main application code
- `student_results.xlsx` – Stores student result records

## Result Calculation

A student is marked **PASS** when they score at least 35 marks in every subject.

The percentage is calculated automatically from the total marks.