"""
Main application flow for the SecurePass Validator project.

This module coordinates name validation, password validation,
blocklist checking, password-history checking, password confirmation,
and Argon2 hashing.
"""

from blocklist import is_password_blocklisted, load_blocklist
from hash_manager import hash_password
from password_history import is_password_reused
from validator import validate_name, validate_password

BLOCKLIST_FILE = "Most-Popular-Letter-Passes.txt"


def display_errors(errors: list[str]) -> None:
    """
    Print each validation error on a separate line.

    Args:
        errors: A list of validation error messages.
    """
    for error in errors:
        print(f"- {error}")


def main() -> None:
    """
    Run the SecurePass Validator application.
    """
    print("SecurePass Validator")
    print("--------------------")

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    name_errors: list[str] = []
    name_errors.extend(validate_name(first_name, "First name"))
    name_errors.extend(validate_name(last_name, "Last name"))

    if name_errors:
        print("\nName validation failed:")
        display_errors(name_errors)
        return

    password_history: list[str] = []

    blocklist = load_blocklist(BLOCKLIST_FILE)

    while True:
        password = input("\nCreate a password: ")

        password_errors = validate_password(
            password,
            first_name,
            last_name,
        )

        if password_errors:
            print("\nPassword validation failed:")
            display_errors(password_errors)
            continue

        if is_password_blocklisted(password, blocklist):
            print(
                "\nPassword rejected: This password appears on the "
                "blocklist and cannot be used. Please try again."
            )
            continue

        if is_password_reused(password, password_history):
            print(
                "\nPassword rejected: This password has been used before "
                "and cannot be reused. Please try again."
            )
            continue

        confirm_password = input("Confirm your password: ")

        if confirm_password != password:
            print(
                "\nPassword confirmation failed: The passwords do not match. "
                "Please try again."
            )
            continue

        break

    stored_hash = hash_password(password)

    password_history.append(stored_hash)

    print(
        "\nPassword accepted. Your password has passed all security checks "
        "and has been securely hashed."
    )


if __name__ == "__main__":
    main()

