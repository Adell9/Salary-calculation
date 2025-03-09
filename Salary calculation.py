
hours = input("Enter the number of working hours: ")
rate = input("What is the rate of effort?:  ")


try:
    hours = float(hours)
    rate = float(rate)
except ValueError:
    print("ERROR: Just enter the numeric inputs.")
    quit()


if hours > 40:
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    total_pay = regular_pay + overtime_pay

else:
    total_pay = hours * rate

print("The total salary is: ",total_pay)
