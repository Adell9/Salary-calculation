while True:
   try:
        hours = float(input("Enter hours: "))
        Rate = float(input("Enter rate: "))
        break
   except ValueError:
       print("ONLY NUMBERS!")



def computepay(hours, Rate):

    if hours > 40:
        overtime_pay = hours - 40
        total_pay = (40*Rate) + overtime_pay * (Rate * 1.5)
    else:
        total_pay = hours * Rate

    return total_pay


print("Pay ",computepay(hours,Rate))


