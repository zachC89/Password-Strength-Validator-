"""
Temporary test runner for the SecurePass Validator blocklist module.

This file tests whether blocklist.py can load the password blocklist
and correctly identify blocked and non-blocked passwords.
"""

from blocklist import load_blocklist, is_password_blocklisted


def main() -> None:
    """
    Run isolated tests for the password blocklist module.
    """
    blocklist = load_blocklist("Most-Popular-Letter-Passes.txt")

    print(f"Loaded {len(blocklist):,} blocklisted passwords.")

    blocked_password = "password"
    safe_password = "River clouds drift after midnight!"

    print(
        f'"{blocked_password}" blocklisted:',
        is_password_blocklisted(blocked_password, blocklist),
    )

    print(
        f'"{safe_password}" blocklisted:',
        is_password_blocklisted(safe_password, blocklist),
    )


if __name__ == "__main__":
    main()
