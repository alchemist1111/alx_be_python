# Prompt the user for their monthly income and monthly expenses
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating the monthly savings
monthly_savings = monthly_income - total_monthly_expenses

# Calculating projected savings after 1 year
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.005)

# Showing monthly savings and projected savings in the terminal
print("Your monthly savings are: ", monthly_savings)
print("Projected savings after one year, with interest, is: ", projected_savings)

