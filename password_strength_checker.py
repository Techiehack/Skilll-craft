import re

def password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    # Uppercase and lowercase letters check
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1

    # Numbers check
    if re.search(r"\d", password):
        score += 1

    # Special characters check
    if re.search(r"[ !\"#$%&'()*+,-./[\\\]^_`{|}~]", password):
        score += 1

    # Additional complexity checks (optional)
    # Custom rules or patterns can be added here based on specific requirements

    return score

def assess_strength(score):
    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Moderate"
    elif score == 3:
        return "Strong"
    elif score >= 4:
        return "Very Strong"

def main():
    print("Password Strength Evaluator")
    print("===========================")
    password = input("Enter a password to assess its strength: ").strip()

    # Calculate password strength score
    score = password_strength(password)

    # Assess and print password strength
    strength = assess_strength(score)
    print(f"The strength of the password '{password}' is: {strength}")

if __name__ == "__main__":
    main()
