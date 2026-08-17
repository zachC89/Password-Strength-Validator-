"""
Password history functionality for the SecurePass Validator project.

This module is responsible for determining whether a proposed new
password matches any previously used password hashes.

It does not store plaintext passwords, perform password validation,
or hash new passwords.
"""

from hash_manager import verify_password


def is_password_reused(
    new_password: str,
    password_history: list[str],
) -> bool:
    """
    Check whether a proposed new password matches any previous password.

    Args:
        new_password: The plaintext password the user wants to use.
        password_history: A list of previously stored Argon2 password hashes.

    Returns:
        True if the new password matches any previous password.
        False if the password has not been used before.
    """
    for stored_hash in password_history:
        if verify_password(new_password, stored_hash):
            return True

    return False