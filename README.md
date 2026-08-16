<p align="center">
  <img src="assets/securepass-banner.png" alt="SecurePass Validator Banner">
</p>


# 🔐 SecurePass Validator

A security-focused Python password validation project designed to demonstrate modern password security concepts, modular software design, and practical Python development.

This project began as a basic password strength analyzer and has evolved into a modular password validation system. The goal is not to build a production authentication platform, but to demonstrate an understanding of password policy, weak-password detection, secure software design, testing, and maintainable Python code.

---

# 🎯 Project Goals

SecurePass Validator is being built to demonstrate practical skills relevant to:

- Security Engineering
- DevSecOps
- Python Development
- Secure Authentication Concepts
- Software Testing
- Git & Version Control

Each feature is developed one sprint at a time using a real software engineering workflow.

---

# ✨ Current Features

## 🔑 Password Validation

The validator currently:

- ✅ Requires passwords between **16–64 characters**
- ✅ Allows letters, numbers, symbols, Unicode characters, and multiple spaces
- ✅ Rejects passwords made entirely of whitespace
- ✅ Rejects passwords containing the user's full first name
- ✅ Rejects passwords containing the user's full last name
- ✅ Uses case-insensitive name detection
- ✅ Returns descriptive validation errors

---

## 🚫 Password Blocklist

The blocklist module currently:

- ✅ Reads password entries from `Most-Popular-Letter-Passes.txt`
- ✅ Loads the blocklist into a Python `set`
- ✅ Uses case-insensitive exact matching
- ✅ Normalizes passwords using `casefold()`
- ✅ Performs average-case **O(1)** lookups
- ✅ Keeps application logic separate from password data

Current blocklist size:

**≈47,603 unique passwords**

---

# 📂 Project Structure

```text
SecurePass-Validator/
│
├── .gitignore
├── blocklist.py
├── hash_manager.py
├── main.py
├── Most-Popular-Letter-Passes.txt
├── password_history.py
├── validator.py
├── README.md
└── LICENSE
```

---

# 🧩 Module Responsibilities

## 🖥️ main.py

Controls the temporary application flow and testing.

---

## 🔍 validator.py

Responsible for:

- Name validation
- Password length validation
- Whitespace validation
- Name detection
- Validation error reporting

---

## 🚫 blocklist.py

Responsible for:

- Loading the blocklist
- Password normalization
- Blocklist lookups

---

## 🔒 hash_manager.py

Reserved for secure password hashing using Argon2.

---

## 📜 password_history.py

Reserved for password history and password reuse detection.

---

# 🛠️ Software Engineering Concepts

This project demonstrates:

- Modular architecture
- Separation of concerns
- Single Responsibility Principle (SRP)
- Helper functions
- Constants
- Type hints
- Docstrings
- Early returns
- File handling
- Context managers
- `pathlib.Path`
- Python Sets
- Hash Tables
- Case-insensitive normalization
- Isolated module testing
- Code reviews
- Refactoring
- Git version control

---

# 🛡️ Security Concepts

Current security concepts implemented include:

- Password length policy
- User-specific password validation
- Password blocklists
- Weak password detection
- Case-insensitive exact matching
- Input validation
- Separation of validation from password storage

---

# 🧪 Testing

Each module is tested independently before integration.

## Validator Tests

- ✅ Empty first name
- ✅ Empty last name
- ✅ Password under 16 characters
- ✅ Password over 64 characters
- ✅ Password containing first name
- ✅ Password containing last name
- ✅ Password containing only spaces
- ✅ Valid password

---

## Blocklist Tests

Verified:

- ✅ Blocklist loads successfully
- ✅ 47,603 passwords loaded
- ✅ Known weak password returns `True`
- ✅ Safe password returns `False`

Example:

```text
"password" → True

"River clouds drift after midnight!" → False
```

---

# ⚙️ Development Workflow

Every sprint follows the same process:

1. 📋 Requirements
2. 🏗️ Design
3. 💻 Implementation
4. 🧪 Testing
5. 👀 Code Review
6. 🔧 Refactoring
7. 📦 Git Commit
8. 📝 Documentation

---

# 🚀 Sprint Progress

## ✅ Sprint 1 — Password Validation Module

Completed:

- Password validation
- Name validation
- Error reporting
- Manual testing
- Code review
- Refactoring
- Git commit

---

## ✅ Sprint 2 — Password Blocklist Module

Completed:

- Blocklist loading
- Python Set implementation
- Case-insensitive normalization
- Exact-match lookups
- Isolated testing
- Documentation improvements
- Git commit

---

# 🧠 Design Decisions

## Why use a Python Set?

The application frequently performs membership lookups.

Python Sets provide approximately **O(1)** lookup performance because they use hash tables internally.

Lists require **O(n)** linear searches.

---

## Why store the blocklist in a text file?

The password list is **data**, not application logic.

Separating them:

- Improves maintainability
- Keeps the source code clean
- Allows updates without changing Python code
- Makes the data reusable by other applications

---

## Why use `casefold()`?

`casefold()` provides Unicode-aware case-insensitive comparisons and is more robust than `lower()`.

---

## Why use `rstrip("\r\n")`?

Using `strip()` could unintentionally modify valid passwords containing spaces.

`rstrip("\r\n")` removes only newline characters.

---

# 📚 What I've Learned

This project has helped reinforce concepts including:

- Modular software design
- Password security best practices
- Python Sets
- Hash Tables
- Big O notation
- File handling
- Context managers
- Git
- Code reviews
- Refactoring
- Technical documentation

---

# 📈 Version History

- **v1.0** – Initial password validation
- **v1.1** – Improved validation structure
- **v1.2** – Password strength scoring
- **SecurePass Redesign** – Modular architecture
- **Sprint 1** – Password Validation Module
- **Sprint 2** – Password Blocklist Module

---

# 🔄 Project Status

🚧 **Actively Developing**

Future modules will include:

- Argon2 password hashing
- Password history
- Password confirmation
- Compromised password detection
- Additional security enhancements

---

# 📄 License

Licensed under the **MIT License**.
