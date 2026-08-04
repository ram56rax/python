num1 = int(input("Enter number: "  ))
operator = input("Enter operator: ")
num2 = int(input("Enter number: "  ))

if operator == "+":
    print(f" the result of {num1} + {num2} = {num1+num2}")
elif operator == "-":
    print(f" the result of {num1} - {num2} = {num1-num2}")
elif operator == "*":
    print(f" the result of {num1} * {num2} = {num1*num2}")
elif operator == "/":
    if num2 !=0:     
     print(f" the result of {num1} / {num2} = {num1/num2}")
    else:
       print("Error: Division by zero is not allowed.")
else:
   print("Invalid operator!")     



