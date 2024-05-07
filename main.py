from lookup_tax import get_tax, find_tax_value
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_user_input(field_name):
    return input(f"{field_name}: ")


def get_yearly_salary():
    while True:
        try:
            return int(get_user_input("Enter Yearly Salary"))
        except ValueError:
            print("Please enter a valid number.")


def get_tax_bracket():
    while True:
        tax_bracket = get_user_input("Enter Tax Bracket")
        if tax_bracket in ["7100", "7101"]:
            return tax_bracket
        print("Invalid tax bracket entered.")


def format_currency(value):
    return f"{value:,.2f}".replace(",", " ").replace(".", ",") + " kr"


def calculate_net_monthly_salary(yearly_salary, tax_bracket):
    tax_table = get_tax(tax_bracket)
    monthly_salary = yearly_salary / 12
    tax_value = find_tax_value(tax_table, monthly_salary)
    net_monthly_salary = monthly_salary - tax_value if tax_value else monthly_salary
    return monthly_salary, tax_value, net_monthly_salary


def display_salaries(monthly_salary, tax_value, net_monthly_salary):
    clear_screen()
    print(f"Monthly Gross Salary: {format_currency(monthly_salary)}")
    print(f"Tax: {format_currency(tax_value)}")
    print(f"Monthly Net Salary: {format_currency(net_monthly_salary)}")


def get_net_monthly_salary():
    yearly_salary = get_yearly_salary()
    tax_bracket = get_tax_bracket()
    return calculate_net_monthly_salary(yearly_salary, tax_bracket)


def rent_calculation(net_salary):
    action = get_user_input("Percentage or Amount?").lower()
    if action == "percentage":
        percentage = float(get_user_input("Enter percentage"))
        max_rent = net_salary * (percentage / 100)
        print(f"Max rent: {format_currency(max_rent)}")
    elif action == "amount":
        amount = float(get_user_input("Enter amount"))
        percentage = (amount / net_salary) * 100
        print(f"Rent is {percentage:.2f}% of your net salary")
    else:
        print("Invalid input")
        rent_calculation(net_salary)


def calculate_50_30_20_rule(net_salary):
    expenses = net_salary * 0.5
    rent = net_salary * 0.3
    expenses_minus_rent = expenses - rent
    wants = net_salary * 0.3
    financial_expenses = net_salary * 0.2
    print(f"Max expenses: {format_currency(expenses)}")
    print(
        f"Where max rent: {format_currency(rent)}, and max expenses minus rent: {format_currency(expenses_minus_rent)}"
    )
    print(f"Max wants: {format_currency(wants)}")
    print(f"Max financial expenses: {format_currency(financial_expenses)}")


def main():
    clear_screen()
    monthly_salary, tax_value, net_monthly_salary = get_net_monthly_salary()
    display_salaries(monthly_salary, tax_value, net_monthly_salary)
    while True:
        action = get_user_input(
            "What do you want to do next? (1: Recalculate, 2: Rent, 3: 50/30/20 rule. Any other key to exit)"
        ).lower()
        if action == "recalculate":
            monthly_salary, tax_value, net_monthly_salary = get_net_monthly_salary()
            display_salaries(monthly_salary, tax_value, net_monthly_salary)
        elif action == "rent":
            rent_calculation(net_monthly_salary)
        elif action == "rule":
            calculate_50_30_20_rule(net_monthly_salary)
        else:
            break


if __name__ == "__main__":
    main()
