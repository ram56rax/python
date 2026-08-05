products= {
    "Apple": 1.00,
    "Flour": 25.16,
    "Eggs": 20.00,
    "Milk": 15.00,
    "Bread": 10.00,
    "Juice": 12.43,

}

print("Welcome to the Price Checker!")
while True:
    product = input("\nEnter a name of the product: (or 'exit' to quit)").strip().capitalize()

    if product.lower() == "exit":
        print("Thank you for using the Price Checker. Goodbye!")
        break
    if product in products:
     print(f"The price of {product} is ${products[product]:.2f}")
    else:
     print("sorry, the product is not found")    
