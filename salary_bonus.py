bonus=float(0.05)
years_worked = float(input("Enter the years worked:"))
salary = float(input("Enter the your salary:"))

if(years_worked>5):
    bonus_amount = salary*bonus
    net_bonus_amount = bonus_amount + salary
    print("Total bonus amount:",bonus_amount)
    print("Total Net bonus amoutn:",net_bonus_amount)
else:
    net_bonus_amount = salary
    print("Total net bonus amount:")

