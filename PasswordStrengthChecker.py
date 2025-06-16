import string

def check_password_strength(password):
    length = len(password)
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in string.punctuation for char in password)

    score = 0

    if length >= 8:
        score += 1
    if lower:
        score += 1
    if upper:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1

    if score == 5:
        return "Strong 💪"
    elif 3 <= score < 5:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

# User input
password = input("Enter your password: ")

# Strength check
strength = check_password_strength(password)

print(f"\nPassword strength: {strength}")
