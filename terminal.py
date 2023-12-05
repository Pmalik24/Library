import mysql.connector
from mysql.connector import Error
import pandas as pd 
from sqlalchemy import create_engine, text
import sys
from sqlalchemy.orm import sessionmaker
import random

host = "localhost"
database = "Library"
# user = "root"
# password = "<>"

def create_connection_string(user, password, host, database):
    return f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

def create_db_engine(user, password, host, database):
    connection_string = create_connection_string(user, password, host, database)
    engine = create_engine(connection_string)
    return engine

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Insert\n2. Update\n3. Delete\n4. View\n5. Return to Main Menu\n6. Exit")
        admin_choice = input("Select an option: ")

        if admin_choice == "1":
            admin_insert_menu()
        elif admin_choice == "2":
            admin_update()
        elif admin_choice == "3":
             admin_delete()
        elif admin_choice == "4":
            admin_view_menu()  # This calls the view submenu
        elif admin_choice == "5":
            return  # This will return to the main menu
        elif admin_choice == "6":
            sys.exit("Exiting the system.")
        else:
            print("Invalid choice, please try again.")

def admin_insert_menu():
    while True:
        print("\nAdmin Insert\Add Menu:")
        print("1. Books\n2. Members\n4. Go Back\n5. Exit\n")
        view_choice = input("Select an option: ")

        if view_choice == "1":
            admin_insert_books()
        elif view_choice == "2":
            admin_insert_members()
        elif view_choice == "3":
            admin_add_librarians()
        elif view_choice == "4":
            return  # This will return to the previous menu (admin_menu)
        elif view_choice == "5":
            sys.exit("Exiting the system.")
        else:
            print("Invalid choice, please try again.")

def admin_insert_books():
    try:
        engine = create_db_engine(user, password, host, database)
        title = input("Enter book title: ")
        author_id = int(input("Enter author ID (0 if not known): "))
        genre_id = int(input("Enter genre ID (0 if not known): "))
        isbn = input("Enter ISBN (leave blank for auto-generation): ")
        publication_year = input("Enter publication year (YYYY-MM-DD): ")

        # Calling the stored procedure
        procedure_call = text("CALL InsertBook(:title, :author_id, :genre_id, :isbn, :publication_year)")
        with engine.connect() as connection:
            connection.execute(procedure_call, {
                'title': title, 
                'author_id': author_id, 
                'genre_id': genre_id, 
                'isbn': isbn, 
                'publication_year': publication_year
            })
            connection.commit()
            print("Book successfully added to the database. Here are the last 10 Books")
            # Fetch and display the latest member(s)
            recent_books_query = text("SELECT * FROM Books ORDER BY Book_ID DESC LIMIT 10")
            recent_books = connection.execute(recent_books_query)
            for book in recent_books:
                # Formatting the date
                formatted_date = book.Publication_Year.strftime('%Y-%m-%d') if book.Publication_Year else 'Unknown'
                print(f"({book.Book_ID}, '{book.Title}', {book.Author_ID}, {book.Genre_ID}, '{book.ISBN}', '{formatted_date}')")

    except Exception as e:
        print(f"An error occurred: {e}")

def admin_insert_members():
    try:
        engine = create_db_engine(user, password, host, database)
        first_name = input("Enter member's first name: ")
        last_name = input("Enter member's last name: ")
        email = input("Enter member's email: ")
        subscription_id = random.randint(1, 3)  # Assuming there are only 3 subscription levels

        insert_query = text("""
            INSERT INTO Members (First_Name, Last_Name, Email, Subscription_ID) 
            VALUES (:first_name, :last_name, :email, :subscription_id)
        """)
        with engine.connect() as connection:
            connection.execute(insert_query, {
                'first_name': first_name, 
                'last_name': last_name, 
                'email': email, 
                'subscription_id': subscription_id
            })
            connection.commit() 
            print("Member successfully added. Here's are the last 5 members:")

            # Fetch and display the latest member(s)
            recent_members_query = text("SELECT * FROM Members ORDER BY Member_ID DESC LIMIT 5")
            recent_members = connection.execute(recent_members_query)
            for member in recent_members:
                print(member)
    except Exception as e:
        print(f"An error occurred: {e}")

def admin_add_librarians():
    try:
        engine = create_db_engine(user, password, host, database)
        first_name = input("Enter librarian's first name: ")
        last_name = input("Enter librarian's last name: ")
        email = input("Enter librarian's email: ")

        insert_query = text("""
            INSERT INTO Librarians (First_Name, Last_Name, Email) 
            VALUES (:first_name, :last_name, :email)
        """)
        with engine.connect() as connection:
            connection.execute(insert_query, {
                'first_name': first_name, 
                'last_name': last_name, 
                'email': email
            })
            connection.commit()
            print("Librarian successfully added.")
            
            # Fetch and display the latest member(s)
            recent_librarians_query = text("SELECT * FROM Librarians ORDER BY Librarian_ID DESC LIMIT 5")
            recent_librarians = connection.execute(recent_librarians_query)
            for member in recent_librarians:
                print(member)
    except Exception as e:
        print(f"An error occurred: {e}")

def admin_view_menu():
    while True:
        print("\nAdmin View Menu:")
        print("1. Books\n2. Members\n3. Go Back\n4. Exit\n")
        view_choice = input("Select an option: ")

        if view_choice == "1":
            admin_view_books()
        elif view_choice == "2":
            admin_view_members()
        elif view_choice == "3":
            return  # This will return to the previous menu (admin_menu)
        elif view_choice == "4":
            sys.exit("Exiting the system.")
        else:
            print("Invalid choice, please try again.")

# Define similar functions for librarian_menu(), member_menu(), etc.

def admin_view_books():
    try:
        engine = create_db_engine(user, password, host, database)
        query = "SELECT * FROM Books"
        df = pd.read_sql(query, engine)
        print(df)
    except Exception as e:
        print(f"An error occurred: {e}")

def admin_view_members():
    try:
        engine = create_db_engine(user, password, host, database)
        query = "SELECT * FROM Members"
        df = pd.read_sql(query, engine)
        print(df)
    except Exception as e:
        print(f"An error occurred: {e}")

def admin_update():
    # Implementation for update functionality
    pass

def admin_delete():
    pass


def librarian_menu():
    while True:
        print("\nLibrarian Menu:")
        print("1. View\n2. Update Availability Status of Books\n3. Return to Main Menu\n4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            librarian_view_menu()
        elif choice == "2":
            librarian_update()
        elif choice == "3":
            return  # This will return to the main menu
        elif choice == "4":
            sys.exit("Exiting the system.")
        else:
            print("Invalid choice, please try again.")

def librarian_view_menu():
        while True:
            print("\nLibrarian View Menu:")
            print("1. Books\n2. Members\n3. Go Back\n4. Exit\n")
            view_choice = input("Select an option: ")

            if view_choice == "1":
                librarian_view_books()
            elif view_choice == "2":
                librarian_view_members()
            elif view_choice == "3":
                return  # This will return to the previous menu (admin_menu)
            elif view_choice == "4":
                sys.exit("Exiting the system.")
            else:
                print("Invalid choice, please try again.")

def librarian_view_books():
    try:
        engine = create_db_engine(user, password, host, database)
        query = "SELECT * FROM Books"
        df = pd.read_sql(query, engine)
        print(df)
    except Exception as e:
        print(f"An error occurred: {e}")

def librarian_view_members():
    try:
        engine = create_db_engine(user, password, host, database)
        query = "SELECT * FROM Members"
        df = pd.read_sql(query, engine)
        print(df)
    except Exception as e:
        print(f"An error occurred: {e}")

def librarian_update():
    pass

def main():
    while True:
        print("Welcome to the Library Management System")
        print("1. Admin\n2. Librarian\n3. Member\n4. Exit")
        choice = input("Select your role: ")

        if choice == "1":
            admin_menu()
        # elif choice == "2":
        #     librarian_menu()
        # elif choice == "3":
        #     member_menu()
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
