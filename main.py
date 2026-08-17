"""
Temporary test runner for the SecurePass Validator password history module.

This file tests whether a proposed new password matches any
previously used Argon2 password hashes.
"""

from hash_manager import hash_password
from password_history import is_password_reused


def main() -> None:
    """
    Run isolated tests for the password history module.
    """
    old_password_one = "River clouds drift after midnight!"
    old_password_two = "Silver lanterns glow near the harbor!"
    old_password_three = "Morning rain falls across the valley!"

    password_history = [
        hash_password(old_password_one),
        hash_password(old_password_two),
        hash_password(old_password_three),
    ]

    reused_password = old_password_two
    new_password = "Golden stars appear above the mountains!"

    print("Reused password test:")
    print(is_password_reused(reused_password, password_history))

    print("\nNew password test:")
    print(is_password_reused(new_password, password_history))


if __name__ == "__main__":
    main()
