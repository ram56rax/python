birth_year = int(input("Enter your birth year:"))
birth_month = int(input("Enter your birth month:"))
birth_day = int(input("Enter your birth day:"))

age_years = 2026 - birth_year
age_months = age_years * 12 + (8 - birth_month)
age_days = age_years * 365 + (8 - birth_month) * 30 + (3 - birth_day)

age_years = age_months // 12
age_months %= 12
age_days %= 30
print (f"Your age is {age_years} years , {age_months} months, and {age_days} days.")

