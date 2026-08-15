def calculate_salary(hours_worked, hourly_rate, tax_rate=0.15):
    # Calculate regular and overtime hours
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    # Calculate earnings
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    gross_salary = regular_pay + overtime_pay
    
    # Calculate deductions
    tax_deduction = gross_salary * tax_rate
    net_salary = gross_salary - tax_deduction
    
    return gross_salary, tax_deduction, net_salary

# User Input
try:
    hours = float(input("Enter total hours worked this week: "))
    rate = float(input("Enter hourly pay rate ($): "))
    
    gross, tax, net = calculate_salary(hours, rate)
    
    # Display Results
    print("\n--- Salary Breakdown ---")
    print(f"Gross Salary:  ${gross:,.2f}")
    print(f"Tax Deduction: ${tax:,.2f}")
    print(f"Net Paycheck:  ${net:,.2f}")

except ValueError:
    print("Please enter valid numerical values.")
