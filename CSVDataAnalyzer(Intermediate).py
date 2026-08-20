import csv

# Sample data mimicking a CSV file structure
csv_data = """Month,Sales
January,15000
February,18500
March,22000
April,14000
May,29000"""

# Parse the CSV data
lines = csv_data.strip().split('\n')
reader = csv.reader(lines)
header = next(reader)  # Skip the header row

total_sales = 0
months_count = 0
high_sales_months = []

for row in reader:
    month = row[0]
    sales = int(row[1])
    
    total_sales += sales
    months_count += 1
    
    # Check for months with sales higher than 20,000
    if sales > 20000:
        high_sales_months.append(month)

# Calculate and display metrics
average_sales = total_sales / months_count
print(f"Average Monthly Sales: ${average_sales:,.2f}")
print(f"High-performing months (> $20k): {', '.join(high_sales_months)}")
