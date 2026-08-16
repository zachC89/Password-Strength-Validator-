"""
Temporary test runner for the SecurePass Validator hash manager.

This file tests password hashing and verification using Argon2.
"""

from hash_manager import hash_password, verify_password


def main() -> None:
    """
    Run isolated tests for the password hashing module.
    """
    test_password = "River clouds drift after midnight!"

    first_hash = hash_password(test_password)
    second_hash = hash_password(test_password)

    print("Original password:")
    print(test_password)

    print("\nFirst Argon2 hash:")
    print(first_hash)

    print("\nSecond Argon2 hash:")
    print(second_hash)

    print("\nDo the two hashes match?")
    print(first_hash == second_hash)

    print("\nCorrect password verification:")
    print(verify_password(test_password, first_hash))

    print("\nIncorrect password verification:")
    print(verify_password("Wrong password example!", first_hash))


if __name__ == "__main__":
    main()
