import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    common_error = password.lower() in ["password", "123456", "qwerty"]

    # Strength logic
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error, common_error]
    score = errors.count(False)

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

# Demo
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength = check_password_strength(pwd)
    print(f"Password strength: {strength}")
