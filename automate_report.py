import csv
from fpdf import FPDF

# Read CSV file
sales_data = []

with open("sales_data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # skip header
    for row in reader:
        sales_data.append([row[0], int(row[1])])

# Calculate total and highest sales
total_sales = sum([row[1] for row in sales_data])
average_sales = total_sales / len(sales_data)

top_seller = max(sales_data, key=lambda x: x[1])

# Create PDF
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Sales Report", ln=True, align="C")

pdf.ln(10)
pdf.set_font("Arial", size=12)

# Table
pdf.cell(90, 10, "Name", 1)
pdf.cell(90, 10, "Sales", 1)
pdf.ln()

for row in sales_data:
    pdf.cell(90, 10, row[0], 1)
    pdf.cell(90, 10, str(row[1]), 1)
    pdf.ln()

pdf.ln(10)

# Summary
pdf.cell(200, 10, f"Total Sales: {total_sales}", ln=True)
pdf.cell(200, 10, f"Average Sales: {round(average_sales,2)}", ln=True)
pdf.cell(200, 10, f"Top Seller: {top_seller[0]} ({top_seller[1]})", ln=True)

pdf.output("Sales_Report.pdf")

print("Report generated successfully!")