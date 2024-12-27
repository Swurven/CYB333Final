import re

def analyze_password(password):
    score = 0
    feedback = []

    # Minimum length check (NIST standard is 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Encourage longer passphrases for stronger security
    if len(password) >= 16:
        score += 1

    # Check for spaces (supporting passphrases)
    if " " in password:
        score += 1

    # Check for a variety of character types (encouraged, not enforced)
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*(),.?\":{}|<>~`" for c in password):
        score += 1

    # Provide user feedback based on password strength
    strength = "Strong" if score >= 5 else "Moderate" if score >= 3 else "Weak"
    if score < 5:
        feedback.append("Consider adding a mix of letters, numbers, and special characters for stronger security.")
    
    return strength, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to analyze: ")
    strength, feedback = analyze_password(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")
