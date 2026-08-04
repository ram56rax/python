print ("Welcome to the BMI calculator!")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}  - You are underweight.")
elif  bmi < 25:
    print(f"Your BMI is {bmi:.2f} -You are in the normal range.")
elif  bmi < 30:
    print(f"Your BMI is {bmi:.2f} - You are overweight.")
else:
    print(f"Your BMI is {bmi:.2f} - You are obese.")
    