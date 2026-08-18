user_name = input(f"Enter username: ")
user_password = input(f"Enter password: ")

def password_strength(password):

    has_uppercase = False

    has_lowercase = False

    digit_count = 0

    special_count = 0

    for character_check in password:
        if character_check.isupper():
            has_uppercase = True

        if character_check.islower():
            has_lowercase = True

        if character_check.isdigit():
            digit_count += 1

        if not character_check.isupper() and not character_check.islower() and not character_check.isdigit():
            special_count += 1

    if len(password) < 8 or len(password) > 16:
        print(f"Password doesn't meet the required length. Please try again. ")

    elif not has_uppercase:
        print(f"Password needs to have an uppercase letter for it to be accepted. ")

    elif not has_lowercase:
        print(f"Password needs to have an lowercase letter for it to be accepted. ")

    elif digit_count < 2:
        print(f"Password needs to have at least 2 numbers in it to be accepted. ")

    elif special_count < 1:
        print(f"Password needs to have a least a special character in it to be accepted. ")

    else:
        strength = len(password)
        if  8 <= strength <= 9:
            print(f"{user_name} your password should be at least 14 characters long. ")
            return f"Very weak password! "

        elif  10 <= strength <= 11:
            print(f"{user_name} your password should be at least 14 characters long. ")
            return f"Weak password! "

        elif 12 <= strength <= 13:
            print(f"{user_name} your password is okay. We recommend a strong password be at least 14 characters long. ")
            return f"You have an okay password. "

        elif 14 <= strength <= 15:
            print(f"{user_name} your password is strong. For a very strong password, it should be 16 characters long. ")
            return f"Strong password! "

        elif strength == 16:
            print(f"{user_name} your password is very strong and matches all of our recommend criteria! Good job!")
            return f"Very strong password! "

password_strength(user_password)