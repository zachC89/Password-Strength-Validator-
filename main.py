"""
Temporary test runner for the SecurePass Validator project.

This file tests the functions currently implemented in validator.py.
It will be expanded later as additional modules are completed.
"""


from validator import validate_name, validate_password


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
    Run the temporary validator test program.
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

    password = input("Create a password: ")

    password_errors = validate_password(
        password,
        first_name,
        last_name,
    )

    if password_errors:
        print("\nPassword validation failed:")
        display_errors(password_errors)
        return

    print("\nPassword passed the current validation rules.")


if __name__ == "__main__":
    main()
