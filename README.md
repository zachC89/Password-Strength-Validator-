# Password Strength Validator (v1.2)

A Python-based password validation tool designed to evaluate password strength using industry-standard security requirements.  
This project is part of my ongoing learning in Python, security fundamentals, and clean software design.

## 🔍 Features
- Validates password length
- Checks for uppercase and lowercase letters
- Ensures at least two digits
- Requires at least one special character
- Returns:
  - Strength percentage
  - List of missing requirements
  - Clear, user-friendly feedback
 
## 🧪 Example Usage

```python
from password_validator import check_password_strength

password = "Hello123!"
percentage, missing = check_password_strength(password)

print("Strength:", percentage)
print("Missing:", missing)

## 🧠 What I Learned
- How to break down validation logic into clean, testable steps
- How to track multiple requirements using counters and flags
- How to return structured data (percentage + missing list)
- How to design functions that scale with future features
- How to think like a security engineer when evaluating password quality

## 🛠️ Tech Used
- Python 3
- Basic string processing
- Conditional logic
- List building and iteration

## 🚀 Future Improvements (v1.3+)
- Add password suggestion generator
- Add customizable password policy (dictionary-based rules)
- Add CLI menu system
- Add color-coded terminal output
- Add logging for audit purposes
- Add random strong password generator

## 📦 Version History
- **v1.0** — Basic validation logic  
- **v1.1** — Cleaner structure, improved return values  
- **v1.2** — Added strength percentage + missing requirement reporting  

## 📚 Purpose
This project helps me build foundational skills for future roles in:
- Security Engineering  
- DevSecOps  
- Python automation  
- Incident response tooling  
