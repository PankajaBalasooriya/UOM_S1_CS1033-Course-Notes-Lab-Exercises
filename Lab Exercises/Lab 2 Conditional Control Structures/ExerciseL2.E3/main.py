consumption = int(input())
fixed_charge = 0
monthly_bill = 0
if consumption <=30:
    fixed_charge = 400
    monthly_bill = fixed_charge + (30 * consumption)
elif consumption <= 60:
    fixed_charge = 550
    monthly_bill = fixed_charge + (30 * 30) + (37 * (consumption - 30))
else:
    monthly_bill = 60 * 42
    if consumption <= 90:
        fixed_charge = 650
        monthly_bill = monthly_bill + fixed_charge + (42 * (consumption - 60))
    elif consumption <= 120:
        fixed_charge = 1500
        monthly_bill = monthly_bill + fixed_charge + (50 * (consumption - 90) + (42 * 30))
    elif consumption <= 180:
        fixed_charge = 1500
        monthly_bill = monthly_bill + fixed_charge + (50 * (consumption - 120) + (42 * 30) + (50 * 30))
    else:
        fixed_charge = 2000
        monthly_bill = monthly_bill + fixed_charge + (75 * (consumption - 180) + (42 * 30) + (50 * 30) + (50 * 60))
print(monthly_bill)
