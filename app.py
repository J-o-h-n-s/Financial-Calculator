from flask import Flask, render_template, request, jsonify
import lookup_tax  # This assumes your tax calculation logic is correctly set up in lookup_tax.py
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tax_brackets=["7100", "7101"])  # Add more brackets as needed

@app.route('/calculate', methods=['POST'])
def calculate():
    salary_type = request.form['salary_type']
    salary_str = request.form['salary']
    salary_str = re.sub(r'[^\d.]', '', salary_str)  # Keep only digits and decimal point
    salary = float(salary_str)
    tax_bracket = request.form['tax_bracket']

    tax_table = lookup_tax.get_tax(tax_bracket)

    if salary_type == 'monthly':
        yearly_salary = salary * 12
    else:
        yearly_salary = salary

    monthly_salary = yearly_salary / 12
    tax_value = lookup_tax.find_tax_value(tax_table, monthly_salary)
    
    # Check if tax_value is None and handle appropriately
    if tax_value is None:
        formatted_tax_value = "No tax data available"
        net_monthly_salary = monthly_salary  # Assume no tax if none found
    else:
        formatted_tax_value = f"{tax_value:,.2f}"
        net_monthly_salary = monthly_salary - tax_value

    return jsonify({
        'yearly_salary': f"{yearly_salary:,.2f}",
        'monthly_salary': f"{monthly_salary:,.2f}",
        'tax_value': formatted_tax_value,
        'net_monthly_salary': f"{net_monthly_salary:,.2f}"
    })


if __name__ == '__main__':
    app.run(debug=True)
