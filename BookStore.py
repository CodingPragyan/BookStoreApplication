from pymongo import MongoClient
import datetime

client = MongoClient()
db = client["Book-Store"]
book_col = db.Books


def add_book():
    book = {}
    isbn = input("ISBN:  ")
    flag = check(isbn)
    if flag < 1:
        book["ISBN"] = isbn
        book["_id"] = book["ISBN"]
        book["TITLE"] = input("TITLE:  ")
        book["AUTHOR ID"] = input("AUTHOR ID:  ")
        book["AUTHOR NAME"] = input("AUTHOR NAME:  ")
        book["AUTHOR ADDRESS"] = input("AUTHOR ADDRESS:  ")
        author_phone = input("AUTHOR PHONE NUMBER:   ")
        flag = check_is_digit(author_phone)
        if flag == 0:
            print("**WARNING!!**  The Author Phone number should be only number")
            return
        else:
            book["AUTHOR PHONE NUMBER"] = author_phone
        book["PUBLISHER ID"] = input("PUBLISHER ID:  ")
        book["PUBLISHER NAME"] = input("PUBLISHER NAME:  ")
        book["PUBLISHER ADDRESS"] = input("PUBLISHER ADDRESS:  ")
        publisher_phone = input("PUBLISHER PHONE NUMBER:   ")
        flag = check_is_digit(publisher_phone)
        if flag == 0:
            print("**WARNING!!**  The Publisher Phone number should be only number")
            return
        else:
            book["PUBLISHER PHONE NUMBER"] = publisher_phone
        price = input("PRICE OF THE BOOK:  ")
        flag = check_is_digit(price)
        if flag == 0:
            print("**WARNING!!**  The Price should be only number")
            return
        else:
            book["PRICE"] = price
        date = input("DATE OF PUBLISHING (DD-MM-YY):  ")
        flag = check_date(date)
        if flag == 0:
            print("**WARNING!!**  Not a valid format of date")
            return
        else:
            book["DATE"] = date
        book_col.insert_one(book)
        print("BOOK INSERTED...")
    else:
        print(" ")
        print("**WARNING!!**  Book with this ISBN already exists...")
        print(" ")


def modify_book():
    isbn = input("Provide the ISBN of the book:  ")
    flag = check(isbn)
    if flag > 0:
        while True:
            print(" ")
            print("MODIFY MENU")
            print("...............")
            print("1. Modify one attribute")
            print("2. Modify whole")
            print("3. Delete a book")
            print("4. Go to Main Menu")
            print("5. QUIT")
            choice1 = input("Enter your choice:  ")
            if choice1 == "1":
                modify_one(isbn)
            elif choice1 == "2":
                modify_all(isbn)
            elif choice1 == "3":
                delete_book(isbn)
            elif choice1 == "4":
                break
            elif choice1 == "5":
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
    if flag > 0:
        print("DISPLAYING BOOK NUMBER " + x)
        print(".............................")
        for i in book_document:
            print(i)
    else:
        print("This book does not exists")
    print(" ")


def display():
    x = book_col.estimated_document_count()
    if x == 0:
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
            flag = check_is_digit(author_phone)
            if flag == 0:
                print("**WARNING!!**  The Author Phone number should be only number")
                return
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
            flag = check_is_digit(publisher_phone)
            if flag == 0:
                print("**WARNING!!**  The Publisher Phone number should be only number")
                return
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
            flag = check_is_digit(price)
            if flag == 0:
                print("**WARNING!!**  The Price should be only number")
                return
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
            date = input("Enter the new publishing DATE (DD-MM-YY)")
            flag = check_date(date)
            if flag == 0:
                print("**WARNING!!**  Not a valid format of date")
                return
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


def check_is_digit(x):
    try:
        num = int(x)
        return 1
    except ValueError:
        return 0


def check_date(x):
    try:
        datetime.datetime.strptime(x, "%d-%m-%Y")
        return 1
    except ValueError:
        return 0


def modify_all(num):
    title = input("TITLE:  ")
    author_id = input("AUTHOR ID:  ")
    author_name = input("AUTHOR NAME:  ")
    author_address = input("AUTHOR ADDRESS:  ")
    author_phone = input("AUTHOR PHONE NUMBER:   ")
    flag = check_is_digit(author_phone)
    if flag == 0:
        print("**WARNING!!**  The Author Phone number should be only number")
        return
    publisher_id = input("PUBLISHER ID:  ")
    publisher_name = input("PUBLISHER NAME:  ")
    publisher_address = input("PUBLISHER ADDRESS:  ")
    publisher_phone = input("PUBLISHER PHONE NUMBER:  ")
    flag = check_is_digit(publisher_phone)
    if flag == 0:
        print("**WARNING!!**  The Publisher Phone number should be only number")
        return
    price = input("PRICE OF THE BOOK:  ")
    flag = check_is_digit(price)
    if flag == 0:
        print("**WARNING!!**  The Price should be only number")
        return
    date = input("DATE OF PUBLISHING(format: DD-MM-YY):  ")
    flag = check_date(date)
    if flag == 0:
        print("**WARNING!!**  Not a valid format of date")
        return

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


def delete_book(x):
    my_query = {"_id": x}
    book_col.delete_one(my_query)
    print(" ")
    print("Book deleted...")
    print(" ")


def check(x):
    query = {"ISBN": x}
    count = book_col.count_documents(query)
    return count


while True:
    print("WELCOME TO BOOK-WORM STORE")
    print("..........................")
    print("1  ADD A BOOK")
    print("2  MODIFY A BOOK")
    print("3  SEARCH A BOOK")
    print("4  DISPLAY LIST OF BOOKS")
    print("5  QUIT")
    choice3 = input("ENTER YOUR OPTION  ")
    if choice3 == "1":
        add_book()
    elif choice3 == "2":
        modify_book()
    elif choice3 == "3":
        search_book()
    elif choice3 == "4":
        display()
    elif choice3 == "5":
        print("Exited BookStore")
        quit()
    else:
        print("**OOPS!!** Invalid Input....")
