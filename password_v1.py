print("Enter a password that contains: Atleast 12 letters, a capitalised letter, a special letter and a number.")

password = (input("Enter your new password: "))

is_valid = False
while not is_valid:

    while len(password) < 12:
        no_length = False
        print("Password is too short, it must contain atleast 12 letters")
        password = (input("Enter your new password: "))

    has_number = False

    for char in password:
        if char.isdigit():
            has_number = True

    while not has_number:
        no_number = False
        password = input("Your password does not contain a number, try again: ")
        for char in password:
            if char.isdigit():
                has_number = True

    has_upper = False

    for char in password:
        if char.isupper():
            has_upper = True

    while not has_upper:
        no_upper = False
        password = input("Your password does not contain a capitalised letter, try again: ")
        for char in password:
            if char.isupper():
                has_upper = True

    allowed = "!@#$%^&*"
    has_special = False

    for char in password:
        if char in allowed:
            has_special = True

    while not has_special:
        no_special = False
        password = input("Your password does not contain a special letter, these are the allowed special letters: '!@#$%^&*' try again: ")
        for char in password:
            if char in allowed:
                has_special = True

    is_valid = True                
    
print("Your password passed all the checks: "+ password)

