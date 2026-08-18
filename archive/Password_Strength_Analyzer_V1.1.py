#Mini Project is now a long-term project
#This is now version V.1.1
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

#Added an Early exit logic that if all above conditions are satisfied the loop can break and
        # not continue to scan for the rest of the characters
        #saves time on long passwords adn makes validator more efficient
        if has_uppercase and has_lowercase and digit_count >= 2 and special_count >= 1:
            break

    if len(password) < 8 or len(password) > 16:
        return f"Password doesn't meet the required length. Please try again. "

#Merged these 2 conditions since it makes the code cleaner and still makes the function act properly
    elif not has_uppercase and not has_lowercase:
        return f"Password needs both an uppercase and lowercase letter for it to be accepted. "

#Did the same with these 2 statements as well
    elif digit_count < 2 and special_count <1:
        return f"Password needs at least 2 numbers and at least a special character in it to be accepted. "

    #v1.1 got rid of print statements that we don't need a.k.a giving it a refactor update
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
#This also allows us to make the function more reusable, for logging, testing, use in another function
#return it from an API
#Finally makes code cleaner and more flexible overall