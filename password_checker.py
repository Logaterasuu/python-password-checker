#Mitt första Python skript!!
import msvcrt
import sys

def get_password_with_stars(prompt=""):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char == b'\x03':
            print("\nProgram exited")
            sys.exit()
        elif char == b'\r' or char == b'\n':
            print()
            break
        elif char == b'\x08':
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            try:
                password += char.decode("utf-8")
                print("*", end="", flush=True)
            except UnicodeDecodeError:
                pass
    return password

print("\nEnter a password that contains: Atleast 12 letters, a capitalised letter, a special letter and a number.\n")
password = get_password_with_stars("Enter your new password: \n")


is_valid = False

while not is_valid:
    is_valid = True
    has_length = False
    has_number = False
    has_capital = False
    has_special = False
    doesnt_match = False

    if len(password) < 12:
        print("Your password needs to be atleast 12 letters.\n")
        has_length = False
        is_valid = False

    for char in password:
            if char.isdigit():
                has_number = True

    if not has_number:
         print("Your password does not contain a number.\n")
         is_valid = False

    for char in password:
            if char.isupper():
                has_capital = True

    if not has_capital:
         print("Your password does not contain a capitalized letter.\n")
         is_valid = False

    allowed = "!@#$%^&*"

    for char in password:
         if char in allowed:
              has_special = True

    if not has_special:
         print("Your password does not contain a special character, these are the special characters allowed: !@#$%^&*\n")
         is_valid = False
    

    if is_valid:
        print("Confirm your new password \n")
        confirm_password = get_password_with_stars()
        if confirm_password == password:
            print("\nYour new password has been set\n")
        else:
             doesnt_match = True
             is_valid = False
             print("\nYour passwords didnt match. Try again, enter your new password: \n")
             password = get_password_with_stars()
             print()

    if not is_valid:
        if not doesnt_match:
            print("Your password does not fullfil the password criteria, try again \n")
            password = get_password_with_stars()
            print()

    
