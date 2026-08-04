birth_year = int(input("Enter your birth year:"))
birth_month = int(input("Enter your birth month:"))
birth_day = int(input("Enter your birth day:"))


age_days = 3-birth_day
age_months = 8-birth_month
age_years = 2026-birth_year

if age_days < 0:
    age_days += 30
    age_months -= 1

if age_months < 0:
    age_months +=12
    age_years -= 1
print (f"Your age is {age_years} years , {age_months} months , and {age_days} days.")

        
