books = [" The Great Gatsby", "To Kill a Mockingbird" , "1984", "Pride and Prejudice", "The Catcher in the Rye"] 
while True:
 print ("Welcome to your books list!")
 print ("What do you want to do?")
 print ("1. Show your books list.")
 print ("2. Add a new book.")
 print ("3. Delete a book.")
 print("-"*30)

 choose = input("Enter a number for task you want to do: ")
 print("-"*30)



 if choose == "1":
    for book in books:
        print(book)

 elif choose == "2":
    new_book = input("Enter the new book you want to add: ")
    books.append(new_book)
    print(f"{new_book} has been added successfully to your books list.")

    print("New books list:")
    for book in books:
        print(book)

 elif choose == "3":
    delete_book = input("Enter the book you want to delete: ")
    if delete_book in books:
        books.remove(delete_book)
        print(f"{delete_book} has been removed successfully from your books list.")

        print("New books list:")
        for book in books:
            print(book)
    else:
     print(f"{delete_book} is not in your books list. ")
 elif choose == "4":
    print("Exiting the program. Goodbye!")
    break
 else:
    print("Invalid choice.")

