from pymongo import MongoClient

client = MongoClient()
db = client["Book-Store"]
book_col = db.Books


def add_book():
    book = {}
    book["ISBN"] = input("ISBN:  ")
    book["_id"] = book["ISBN"]
    book["TITLE"] = input("TITLE:  ")
    book["AUTHOR ID"] = input("AUTHOR ID:  ")
    book["AUTHOR NAME"] = input("AUTHOR NAME:  ")
    book["AUTHOR ADDRESS"] = input("AUTHOR ADDRESS:  ")
    book["AUTHOR PHONE NUMBER"] = input("AUTHOR PHONE NUMBER:   ")
    book["PUBLISHER ID"] = input("PUBLISHER ID:  ")
    book["PUBLISHER NAME"] = input("PUBLISHER NAME:  ")
    book["PUBLISHER ADDRESS"] = input("PUBLISHER ADDRESS:  ")
    book["PUBLISHER PHONE NUMBER"] = input("PUBLISHER PHONE NUMBER:  ")
    book["PRICE"] = int(input("PRICE OF THE BOOK:  "))
    book["DATE"] = input("DATE OF PUBLISHING:  ")
    book_col.insert_one(book)
    print("BOOK INSERTED...")

    
def modify_book():
    isbn = input("Provide the ISBN of the book:  ")
    flag = check(isbn)
    if flag > 0:
        while True:
            print("MODIFY MENU")
            print("...............")
            print("1. Modify one attribute")
            print("2. Modify whole")
            print("3. Go to Main Menu")
            print("4. QUIT")
            choice1 = input("Enter your choice:  ")
            if choice1 == "1":
                modify_one(isbn)
            elif choice1 == "2":
                modify_all(isbn)
            elif choice1 == "3":
                break
            elif choice1 == "4":
                quit()
            else:
                print("**OOPS!!**  Invalid input....")
    else:
        print("ISBN not found. Book does not exist")


def search_book():
    x = input("Enter the book ISBN:  ")
    flag = check(x)
    query = {"ISBN": x}
    book_document = book_col.find(query)
    print(" ")
    print("DISPLAYING BOOK NUMBER "+x)
    print(".............................")
    if flag > 0:
        for i in book_document:
            print(i)
    else:
        print("This book does not exists")
    print(" ")


def display():
    x = book_col.estimated_document_count()
    if x < 1:
        print("NO BOOK ADDED IN THE DATABASE")
    count = book_col.find({})
    print(" ")
    print("DISPLAYING ALL BOOKS")
    print(".......................")
    for document in count:
        print(document)
    print(" ")


def modify_one(num):
    while True:
        print("MODIFY MENU(specific)")
        print(".......................")
        print("1. TITLE")
        print("2. AUTHOR ID")
        print("3. AUTHOR NAME")
        print("4. AUTHOR ADDRESS")
        print("5. AUTHOR PHONE NUMBER")
        print("6. PUBLISHER ID")
        print("7. PUBLISHER NAME")
        print("8. PUBLISHER ADDRESS")
        print("9. PUBLISHER PHONE NUMBER")
        print("10. PRICE OF THE BOOK")
        print("11. DATE OF PUBLISHING")
        print("12. Go to the Previous Menu")
        print("13. QUIT")
        choice2 = input("Enter your choice")
        if choice2 == "1":
            title = input("Enter the new TITLE")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "TITLE": title
                    }
                }
            )
            print("TITLE updated...")
        elif choice2 == "2":
            author_id = input("Enter the new AUTHOR ID")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "AUTHOR ID": author_id
                    }
                }
            )
            print("AUTHOR ID updated...")
        elif choice2 == "3":
                author_name = input("Enter the new AUTHOR NAME")
                book_col.update_one(
                    {"_id": num},
                    {
                        "$set": {
                            "AUTHOR NAME": author_name
                        }
                    }
                )
                print("AUTHOR NAME updated...")
        elif choice2 == "4":
            author_address = input("Enter the new AUTHOR ADDRESS")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "AUTHOR ADDRESS": author_address
                    }
                }
            )
            print("AUTHOR ADDRESS updated...")
        elif choice2 == "5":
            author_phone = input("Enter the new AUTHOR PHONE NUMBER")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "AUTHOR PHONE NUMBER": author_phone
                    }
                }
            )
            print("AUTHOR PHONE NUMBER updated...")
        elif choice2 == "6":
            publisher_id = input("Enter the new PUBLISHER ID")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "PUBLISHER ID": publisher_id
                    }
                }
            )
            print("PUBLISHER ID updated...")
        elif choice2 == "7":
            publisher_name = input("Enter the new PUBLISHER NAME")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "PUBLISHER NAME": publisher_name
                    }
                }
            )
            print("PUBLISHER NAME updated...")
        elif choice2 == "8":
            publisher_address = input("Enter the new PUBLISHER ADDRESS")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "PUBLISHER ADDRESS": publisher_address
                    }
                }
            )
            print("PUBLISHER ADDRESS updated...")
        elif choice2 == "9":
            publisher_phone = input("Enter the new PUBLISHER PHONE NUMBER")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "PUBLISHER PHONE NUMBER": publisher_phone
                    }
                }
            )
            print("PUBLISHER PHONE NUMBER updated...")
        elif choice2 == "10":
            price = input("Enter the new PRICE of the book")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "PRICE": price
                    }
                }
            )
            print("PRICE updated...")
        elif choice2 == "11":
            date = input("Enter the new publishing DATE")
            book_col.update_one(
                {"_id": num},
                {
                    "$set": {
                        "DATE": date
                    }
                }
            )
            print("Publishing DATE updated...")
        elif choice2 == "12":
            break
        elif choice2 == "13":
            quit()
        else:
            print("**OOPS!!**   Invalid input.....")


def modify_all(num):
    title = input("TITLE:  ")
    author_id = input("AUTHOR ID:  ")
    author_name = input("AUTHOR NAME:  ")
    author_address = input("AUTHOR ADDRESS:  ")
    author_phone = input("AUTHOR PHONE NUMBER:   ")
    publisher_id = input("PUBLISHER ID:  ")
    publisher_name = input("PUBLISHER NAME:  ")
    publisher_address = input("PUBLISHER ADDRESS:  ")
    publisher_phone = input("PUBLISHER PHONE NUMBER:  ")
    price = int(input("PRICE OF THE BOOK:  "))
    date = input("DATE OF PUBLISHING:  ")

    book_col.update_many(
        {"_id": num},
        {
            "$set": {
                "TITLE": title,
                "AUTHOR ID": author_id,
                "AUTHOR NAME": author_name,
                "AUTHOR ADDRESS": author_address,
                "AUTHOR PHONE NUMBER": author_phone,
                "PUBLISHER ID": publisher_id,
                "PUBLISHER NAME": publisher_name,
                "PUBLISHER ADDRESS": publisher_address,
                "PUBLISHER PHONE NUMBER": publisher_phone,
                "PRICE": price,
                "DATE": date
            }
        }
    )


def check(x):
    query = {"ISBN": x}
    count = book_col.count_documents(query)
    return count


def admin_login():
    while True:
        print("Welcome ADMIN. Choose your options")
        print("..................................")
        print("1  ADD A BOOK")
        print("2  MODIFY A BOOK")
        print("3  SEARCH A BOOK")
        print("4  DISPLAY LIST OF BOOKS")
        print("5  GO TO THE HOME PAGE")
        print("6  QUIT")
        choice3 = input("ENTER YOUR OPTION  ")
        if choice3 == "1":
            add_book()
        elif choice3 == "2":
            modify_book()
            print("Book Store successfully updated.....")
        elif choice3 == "3":
            search_book()
        elif choice3 == "4":
            display()
        elif choice3 == "5":
            break
        elif choice3 == "6":
            print("Exited BookStore")
            quit()
        else:
            print("**OOPS!!** Invalid Input....")


def read_book():
    print("Hope you enjoyed reading the book")


def user_login():
    while True:
        print("Welcome USER. Choose your options")
        print(".................................")
        print("1.  READ eBOOK")
        print("2.  SEARCH FOR A BOOK")
        print("3.  DISPLAY ALL BOOKS")
        print("4.  GO TO HOME PAGE")
        print("5.  QUIT")
        x = input("Enter your option here:  ")
        if x == "1":
            search_book()
            z = input("Here is your soft copy of the book. Enjoy reading!! Press 1 if you are done:  ")
            print(" ")
            if z == "1":
                pass
            else:
                print("**OOPS!!** Invalid Input....")
        elif x == "2":
            search_book()
            y = input("Do you want to read it [Y/N]?")
            if y.lower() == "y":
                read_book()
            elif y.lower() == "n":
                break
            else:
                print("**OOPS!!** Invalid Input....")
        elif x == "3":
            display()
        elif x == "4":
            break
        elif x == "5":
            quit()
        else:
            print("**OOPS!!** Invalid Input....")


while True:
    print("Welcome to BOOK WORM, Read your favorite book online")
    print("****************************************************")
    print("Press 1 for USER LOGIN")
    print("Press 2 for ADMIN LOGIN")
    print("Press 3 to EXIT")
    choice = input("Enter your choice here:  ")
    if choice == "1":
        print(">>>You have login as a user<<<")
        user_login()
    elif choice == "2":
        print(">>>You have login as an admin<<<")
        admin_login()
    elif choice == "3":
        quit()
    else:
        print("**OOPS!!** Invalid Input....")
