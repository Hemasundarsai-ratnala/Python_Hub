d = int(input())
years = d//365
rem_days = d%365
months = rem_days//30
rem_days = rem_days%30
days = rem_days
print("No. of years :",years)
print("No. of months :",months)
print("No. of days :",days)
