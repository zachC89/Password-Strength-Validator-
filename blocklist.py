"""
Password blocklist logic for the SecurePass Validator project.

This module loads prohibited passwords from a text file and checks
whether a user-selected password appears on the blocklist.
"""

from pathlib import Path


def load_blocklist(file_path: str | Path) -> set[str]:
    """
    Load passwords from a text file into a normalized set.

    Each non-empty line in the file represents one prohibited password.
    Passwords are normalized using casefold() so blocklist comparisons
    are case-insensitive.

    Args:
        file_path: Path to the password blocklist text file.

    Returns:
        A set containing normalized prohibited passwords.

    Raises:
        FileNotFoundError: If the blocklist file cannot be found.
    """
    blocklist: set[str] = set()

    path = Path(file_path)

    with path.open("r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            password = line.rstrip("\r\n")

            if password:
                blocklist.add(password.casefold())

    return blocklist


def is_password_blocklisted(
    password: str,
    blocklist: set[str],
) -> bool:
    """
    Check whether a password appears on the blocklist.

    Comparison is case-insensitive exact matching.

    Args:
        password: Password selected by the user.
        blocklist: Set of normalized prohibited passwords.

    Returns:
        True if the password appears on the blocklist.
        Otherwise, False.
    """
    normalized_password = password.casefold()

    return normalized_password in blocklist