#Mini Project
user_name = input(f"Enter username: ")
user_password = input(f"Enter password: ")
#function receives 1 parameter, the password
#basic function structure before going into looping for each variable later
#have all the tracking variables we need
#placement order matters since python reads code from top to bottom

def password_strength(password):
            #uppercase letter for password auto default to false
    has_uppercase = False

            #lowercase letter for password auto default to false
    has_lowercase = False

            #how many numbers in password auto default to 0
    digit_count = 0

        #special character for password
    special_count = 0

    #This loop is now checking for all the right conditions for the password before moving to length/strength conditions
    for character_check in password:
        if character_check.isupper():
            has_uppercase = True
            #This checks to see if the password has an uppercase letter

        if character_check.islower():
            has_lowercase = True
            #This checks to see if the password has a lowercase letter

        if character_check.isdigit():
            digit_count += 1
                #This is checking for how many numbers in the password

        if not character_check.isupper() and not character_check.islower() and not character_check.isdigit():
            special_count += 1
                    # This checks to see if password has a special character or not


    #Setting password length condition
    if len(password) < 8 or len(password) > 16:
        print(f"Password doesn't meet the required length. Please try again. ")

    elif not has_uppercase:
        print(f"Password needs to have an uppercase letter for it to be accepted. ")
            #if user doesn't have an uppercase the program tells us we need one for it to be accepted

    elif not has_lowercase:
        print(f"Password needs to have an lowercase letter for it to be accepted. ")
            #if user doesn't have a lowercase the program tells us we need one for it to be accepted

    elif digit_count < 2:
        print(f"Password needs to have at least 2 numbers in it to be accepted. ")
            #if user doesn't have at least 2 numbers, the program tells us we need at least 2 for it to be accepted


    elif special_count < 1:
        print(f"Password needs to have a least a special character in it to be accepted. ")
        # if user doesn't have at least 1 special character, the program tells us we need at least 1 for it to be accepted

    #This statement is telling us that the length of the password will determine how weak or strong it is
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
        #Program prints {username} your password {password} is very weak, weak, okay, strong, or very strong.

password_strength(user_password)


