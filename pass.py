# Python script that allows you to input a password and it will test the strength of the password 

import pyperclip
from passwordlib import util as pwutil
from passwordlib.commonly_used import is_commonly_used
from passwordlib.analyzer import Analyzer
from getpass import getpass

# Load common passwords from a text file
def load_common_passwords(file_path):
    with open(file_path, 'r') as file:
        return {line.strip() for line in file}

# Append weak password to the common passwords file
def append_to_common_passwords(file_path, password):
    with open(file_path, 'a') as file:
        file.write(password + '\n')

common_passwords = load_common_passwords('common_passwords.txt')

while True:
    password = getpass("Input your password here: ")
    
    if password in common_passwords:
        print("Your password is commonly used. Please choose a different one.")
        continue  # Prompt for a new password

    result = Analyzer(password)

    if result.is_secure:
        if result.is_highly_secure:
            print("Password is highly secure!")
        else:
            print("Your password is secure but could be better!")
        print(f"Your password score is {result.score} out of 10.")
        break  # Exit the loop if the password is secure
    else:
        print("Your password is not secure. Please try again.")
        if result.is_commonly_used:
            print("Warning: Your password is commonly used. Please choose a different one.")
    
    # Append weak password to the common passwords file
    append_to_common_passwords('common_passwords.txt', password)

pyperclip.copy(password)
print("Your password is copied to your clipboard")
print("Don't forget to keep it safe! Enjoy!")
