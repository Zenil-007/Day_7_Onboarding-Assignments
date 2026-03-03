🚀 Project Overview

This project implements a Personal Finance Calculator designed for an AI startup’s employee benefits portal.

The program collects salary and expense details from users, validates inputs, performs financial calculations, and generates a professional formatted financial summary.

The objective of this assignment was to demonstrate:

Proper variable naming (PEP 8)

Understanding of Python data types (int, float, str, bool)

Type validation and casting

f-string formatting

Input validation

Modular function design

Git workflow and version control practices

🎯 Features Implemented
✅ Core Functionality (Part A)

Collects:

Employee name

Annual salary

Tax percentage

Monthly rent

Savings goal percentage

Validates:

Salary > 0

Tax between 0–50%

Rent > 0

Savings goal between 0–100%

Calculates:

Monthly gross salary

Monthly tax deduction

Net salary

Rent ratio

Monthly savings amount

Disposable income

Annual projections

Generates a professionally formatted financial report using f-strings.

🚀 Stretch Features (Part B)

Indian number formatting (₹12,00,000 format)

Comparison between two employees

Financial Health Score (0–100) based on:

Rent ratio

Savings rate

Disposable income percentage

🧠 Interview Readiness (Part C)

Deep understanding of:

Type system behavior

type() vs isinstance()

Float precision (0.1 + 0.2)

Truthiness evaluation

Custom function:

analyze_value(value) for dynamic type inspection

Debugging common type and formatting errors

🤖 AI-Augmented Learning (Part D)

Generated a Python type conversion matrix using AI

Tested each conversion in Python

Critically evaluated AI accuracy and identified edge cases

🛠 Technologies & Concepts Used

Python 3.x

Data types (int, float, str, bool)

Type casting

f-strings formatting

Input validation

Conditional logic

Git & GitHub workflow

Pylint (≥ 7/10)

Black code formatter

📂 Project Structure
.
├── finance_calculator.py
├── requirements.txt (if applicable)
├── README.md
└── (Optional) sample_output.txt
▶️ How to Run
python finance_calculator.py

Follow the prompts to enter salary and expense details.

📈 Sample Output Format
════════════════════════════════════════════
EMPLOYEE FINANCIAL SUMMARY
════════════════════════════════════════════
Employee : Priya Sharma
Annual Salary : ₹12,00,000.00
────────────────────────────────────────────
Monthly Breakdown:
Gross Salary : ₹ 1,00,000.00
Tax (30.0%) : ₹ 30,000.00
Net Salary : ₹ 70,000.00
Rent : ₹ 25,000.00 (35.7% of net)
Savings (20.0%) : ₹ 14,000.00
Disposable : ₹ 31,000.00
────────────────────────────────────────────
Annual Projection:
Total Tax : ₹ 3,60,000.00
Total Savings : ₹ 1,68,000.00
Total Rent : ₹ 3,00,000.00
════════════════════════════════════════════
🧩 Key Learning Outcomes

Through this assignment, I strengthened:

1. Understanding of Python’s type system

2. Precision handling of floating-point arithmetic

3. Writing clean, modular code

4. Input validation best practices

5. Professional formatting standards

6. Git version control discipline

7. Critical evaluation of AI-generated content
