import mysql.connector
from mysql.connector import Error
import pandas as pd 
from sqlalchemy import create_engine, text
import sys
from sqlalchemy.orm import sessionmaker

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
            admin_insert()
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
            break
        else:
            print("Invalid choice, please try again.")


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

def admin_delete():
    pass

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

def admin_insert():
    # Implementation for insert functionality
    pass

def admin_update():
    # Implementation for update functionality
    pass

# ... other specific functions for each action ...

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
