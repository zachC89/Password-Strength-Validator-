"""
Password validation logic for the SecurePass Validator project.

This module validates user names and password policy requirements.
It does not perform password hashing, blocklist checking, or storage.
"""

MIN_PASSWORD_LENGTH = 16
MAX_PASSWORD_LENGTH = 64


def validate_name(name: str, field_name: str) -> list[str]:
    """
    Validate a first-name or last-name input.

    Args:
        name: The name entered by the user.
        field_name: The label used in the error message, such as
            "First name" or "Last name".

    Returns:
        A list of validation error messages. An empty list means
        the name passed validation.
    """
    errors: list[str] = []

    if not name.strip():
        errors.append(f"{field_name} cannot be empty. Please try again.")

    return errors


def password_contains_name(
    password: str,
    first_name: str,
    last_name: str,
) -> bool:
    """
    Check whether a password contains the user's full first or last name.

    Comparisons are case-insensitive.

    Examples rejected for first name 'Jordan' and last name 'Thompson':

        MyPasswordJordan!
        THOMPSON-secure-pass
        JordanThompsonPassword
        ThompsonJordanPassword

    Args:
        password: The password selected by the user.
        first_name: The user's first name.
        last_name: The user's last name.

    Returns:
        True when the password contains prohibited name information.
        Otherwise, False.
    """
    normalized_password = password.casefold()
    normalized_first = first_name.strip().casefold()
    normalized_last = last_name.strip().casefold()

    if normalized_first and normalized_first in normalized_password:
        return True

    if normalized_last and normalized_last in normalized_password:
        return True

    return False


def validate_password(
    password: str,
    first_name: str,
    last_name: str,
) -> list[str]:
    """
    Validate a password against the project's password policy.

    Current rules:

    - Password must contain between 16 and 64 characters.
    - Password cannot consist entirely of whitespace.
    - Password cannot contain the user's full first or last name.

    Letters, numbers, symbols, Unicode characters, and multiple spaces
    are otherwise permitted.

    Args:
        password: The password selected by the user.
        first_name: The user's first name.
        last_name: The user's last name.

    Returns:
        A list of validation error messages. An empty list means
        the password passed this module's validation checks.
    """
    errors: list[str] = []
    password_length = len(password)

    if password_length < MIN_PASSWORD_LENGTH:
        errors.append(
            "Password does not meet the minimum password length "
            f"requirement. Password must be at least "
            f"{MIN_PASSWORD_LENGTH} characters long. Please try again."
        )

    if password_length > MAX_PASSWORD_LENGTH:
        errors.append(
            "Password exceeds the maximum password length requirement. "
            f"Password cannot be more than "
            f"{MAX_PASSWORD_LENGTH} characters long. Please try again."
        )

    if password and password.isspace():
        errors.append(
            "Password cannot consist entirely of spaces. "
            "Please create a password containing visible characters."
        )

    if password_contains_name(password, first_name, last_name):
        errors.append(
            "Password cannot contain the user's full first or last name. "
            "Please create a different password."
        )

    return errors