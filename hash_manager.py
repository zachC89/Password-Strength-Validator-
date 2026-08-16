"""
Password hashing functionality for the SecurePass Validator project.

This module is responsible for securely hashing accepted passwords
using Argon2 and verifying passwords against stored password hashes.

It does not perform password validation, blocklist checking,
or password history management.
"""

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerifyMismatchError


password_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    """
    Hash a plaintext password using Argon2.

    Args:
        password: The plaintext password to hash.

    Returns:
        The encoded Argon2 password hash.
    """
    return password_hasher.hash(password)


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verify a plaintext password against a stored Argon2 hash.

    Args:
        password: The plaintext password entered by the user.
        stored_hash: The previously stored Argon2 password hash.

    Returns:
        True if the password matches the stored hash.
        False if the password does not match or the stored hash is invalid.
    """
    try:
        return password_hasher.verify(stored_hash, password)

    except (VerifyMismatchError, InvalidHashError):
        return False