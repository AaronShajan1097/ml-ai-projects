month = ["January","February","March","April","May"]
expense = [2200,2350,2600,2130,2190]

# Extra money spent in February compared to January
feb_jan_spent = expense[1] - expense[0]
print(f"1. Extra Money Spent on February compared to January: {feb_jan_spent}$")

# Total expense in the first quarter (first three months)
first_quarter_expense = 0
for exp in range(3):
    first_quarter_expense+= expense[exp]
print(f"2. First Quarter Expense: {first_quarter_expense}$")

# Check if exactly $2000 was spent in any month
spent_2000 = 0
if 2000 in expense:
    spent_2000+= 1
    print(f"Spent Exactly 2000 Dollars in a Month")
else:
    print("No")

# Add June month expense ($1980)
month.append("June")
expense.append(1980)
print(month)
print(expense)

# Correct April expense after $200 refund
expense[3] = 1930
print(f"{expense[3]}$")