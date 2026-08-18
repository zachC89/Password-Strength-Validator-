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

        if has_uppercase and has_lowercase and digit_count >= 2 and special_count >= 1:
            break

    if len(password) < 8 or len(password) > 16:
        return f"Password doesn't meet the required length. Please try again. "

    elif not has_uppercase and not has_lowercase:
        return f"Password needs both an uppercase and lowercase letter for it to be accepted. "

#Did the same with these 2 statements as well
    elif digit_count < 2 and special_count <1:
        return f"Password needs at least 2 numbers and at least a special character in it to be accepted. "

    else:
        strength = len(password)
        if  8 <= strength <= 9:
            return f"{user_name} your password should be at least 14 characters long. "

        elif  10 <= strength <= 11:
            return f"{user_name} your password should be at least 14 characters long. "

        elif 12 <= strength <= 13:
            return f"{user_name} your password is okay. We recommend a strong password be at least 14 characters long. "

        elif 14 <= strength <= 15:
            return f"{user_name} your password is strong. For a very strong password, it should be 16 characters long. "

        elif strength == 16:
            return f"{user_name} your password is very strong and matches all of our recommend criteria! Good job!"

result = password_strength(user_password)
print(result)