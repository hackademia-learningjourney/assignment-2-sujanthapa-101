# Sujan Thapa - Assignment 2
import json
import os

USER_DATA_FILE = 'user_data.json'

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def sign_up():
    username = input("Enter username: ")
    
    user_data = load_user_data()
    if username in user_data:
        print("Username already exists. Please try again.")
        return

    password = input("Enter password: ")
    mobile_number = input("Enter mobile number: ")
    user_data[username] = { 'password': password, 'mobile_number': mobile_number }

    save_user_data(user_data)
    print("Sign up successful!")

def sign_in():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_data = load_user_data()
    if username in user_data and user_data[username]['password'] == password:
        print(f"Welcome to the device, {username}!")
        print(f"Your mobile number is: {user_data[username]['mobile_number']}")
    else:
        print("Incorrect credentials.")

def main():
    while(True):
        print("1. Sign up")
        print("2. Sign in")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
        else:
            print("Invalid choice. Program terminated.")
            break

if __name__ == "__main__":
    main()
