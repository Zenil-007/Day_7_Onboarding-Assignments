"""
Personal Finance Calculator
Day 7 PM Assignment – Variables, Data Types & Git

Includes:
- Financial breakdown
- Indian number formatting
- Two employee comparison
- Financial health score (0-100)
"""


def format_indian_currency(amount):
    """Format number in Indian numbering system."""
    amount = float(amount)
    integer_part, decimal_part = f"{amount:.2f}".split(".")

    if len(integer_part) <= 3:
        formatted = integer_part
    else:
        last_three = integer_part[-3:]
        remaining = integer_part[:-3]
        parts = []
        while len(remaining) > 2:
            parts.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            parts.insert(0, remaining)
        formatted = ",".join(parts) + "," + last_three

    return f"₹{formatted}.{decimal_part}"


def get_valid_float(prompt, min_value=None, max_value=None):
    """Validate float input within optional bounds."""
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value <= min_value:
                print(f"Value must be greater than {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must not exceed {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_financials(
    annual_salary,
    tax_percentage,
    monthly_rent,
    savings_percentage,
):
    """Perform financial calculations."""
    monthly_salary = annual_salary / 12
    monthly_tax = monthly_salary * (tax_percentage / 100)
    net_salary = monthly_salary - monthly_tax
    savings_amount = net_salary * (savings_percentage / 100)
    disposable_income = net_salary - monthly_rent - savings_amount
    rent_ratio = (monthly_rent / net_salary) * 100 if net_salary > 0 else 0

    return {
        "monthly_salary": monthly_salary,
        "monthly_tax": monthly_tax,
        "net_salary": net_salary,
        "savings_amount": savings_amount,
        "disposable_income": disposable_income,
        "rent_ratio": rent_ratio,
        "annual_tax": monthly_tax * 12,
        "annual_savings": savings_amount * 12,
        "annual_rent": monthly_rent * 12,
    }


def calculate_health_score(rent_ratio, savings_percentage, disposable_ratio):
    """
    Financial health score (0-100).
    Formula:
    - Rent ratio < 30% → +30 points
    - Savings rate ≥ 20% → +35 points
    - Disposable ≥ 20% → +35 points
    """
    score = 0

    if rent_ratio < 30:
        score += 30
    elif rent_ratio < 40:
        score += 20
    else:
        score += 10

    if savings_percentage >= 20:
        score += 35
    elif savings_percentage >= 10:
        score += 20
    else:
        score += 10

    if disposable_ratio >= 20:
        score += 35
    elif disposable_ratio >= 10:
        score += 20
    else:
        score += 10

    return min(score, 100)


def generate_report(
    name, annual_salary, tax_percentage, savings_percentage, monthly_rent, data
):
    """Generate formatted employee report."""
    line = "════════════════════════════════════════════"
    separator = "────────────────────────────────────────────"

    disposable_ratio = (
        (data["disposable_income"] / data["net_salary"]) * 100
        if data["net_salary"] > 0
        else 0
    )

    health_score = calculate_health_score(
        data["rent_ratio"],
        savings_percentage,
        disposable_ratio,
    )

    report = f"""
{line}
EMPLOYEE FINANCIAL SUMMARY
{line}
Employee : {name}
Annual Salary : {format_indian_currency(annual_salary)}
{separator}
Monthly Breakdown:
Gross Salary : {format_indian_currency(data['monthly_salary'])}
Tax ({tax_percentage}%) : {format_indian_currency(data['monthly_tax'])}
Net Salary : {format_indian_currency(data['net_salary'])}
Rent : {format_indian_currency(monthly_rent)} ({data['rent_ratio']:.1f}% of net)
Savings ({savings_percentage}%) : {format_indian_currency(data['savings_amount'])}
Disposable : {format_indian_currency(data['disposable_income'])}
Financial Health Score : {health_score}/100
{separator}
Annual Projection:
Total Tax : {format_indian_currency(data['annual_tax'])}
Total Savings : {format_indian_currency(data['annual_savings'])}
Total Rent : {format_indian_currency(data['annual_rent'])}
{line}
"""
    return report, health_score


def collect_employee_data():
    """Collect and return employee input data."""
    name = input("\nEnter employee name: ")

    annual_salary = get_valid_float(
        "Enter annual salary: ",
        min_value=0,
    )

    tax_percentage = get_valid_float(
        "Enter tax percentage (0-50): ",
        min_value=-1,
        max_value=50,
    )

    monthly_rent = get_valid_float(
        "Enter monthly rent: ",
        min_value=0,
    )

    savings_percentage = get_valid_float(
        "Enter savings goal percentage (0-100): ",
        min_value=-1,
        max_value=100,
    )

    financial_data = calculate_financials(
        annual_salary,
        tax_percentage,
        monthly_rent,
        savings_percentage,
    )

    return (
        name,
        annual_salary,
        tax_percentage,
        savings_percentage,
        monthly_rent,
        financial_data,
    )


def compare_employees(emp1, emp2):
    """Display side-by-side comparison."""
    print("\n================ EMPLOYEE COMPARISON ================")
    print(f"{emp1[0]:<20} | {emp2[0]:<20}")
    print("-" * 50)
    print(
        f"Annual Salary: {format_indian_currency(emp1[1]):<20} | "
        f"{format_indian_currency(emp2[1]):<20}"
    )
    print(
        f"Net Monthly: {format_indian_currency(emp1[5]['net_salary']):<20} | "
        f"{format_indian_currency(emp2[5]['net_salary']):<20}"
    )
    print("=" * 50)


def main():
    """Main execution."""
    print("\n=== Personal Finance Calculator ===")

    employee1 = collect_employee_data()
    report1, _ = generate_report(*employee1)
    print(report1)

    choice = input("Would you like to compare with another employee? (y/n): ")

    if choice.lower() == "y":
        employee2 = collect_employee_data()
        report2, _ = generate_report(*employee2)
        print(report2)
        compare_employees(employee1, employee2)


if __name__ == "__main__":
    main()
