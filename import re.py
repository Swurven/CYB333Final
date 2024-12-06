import re

def evaluate_password(password):
    """
    Evaluates the strength of a password and provides feedback.
    Returns a score and improvement suggestions.
    """

    # Criteria and their corresponding scores
    length_criteria = len(password) >= 12
    lower_criteria = any(char.islower() for char in password)
    upper_criteria = any(char.isupper() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Common password patterns
    common_patterns = [
        "password", "12345", "qwerty", "abc123", "letmein", "admin", "welcome"
    ]
    common_criteria = any(pattern in password.lower() for pattern in common_patterns)

    # Calculate score
    score = sum([
        length_criteria, lower_criteria, upper_criteria,
        digit_criteria, special_criteria
    ])
    
    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Increase password length to at least 12 characters.")
    if not lower_criteria:
        feedback.append("Add lowercase letters.")
    if not upper_criteria:
        feedback.append("Include uppercase letters.")
    if not digit_criteria:
        feedback.append("Use at least one numeric digit.")
    if not special_criteria:
        feedback.append("Include special characters (e.g., !, @, #).")
    if common_criteria:
        feedback.append("Avoid using common patterns or phrases like 'password123'.")
    
    # Strength rating
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

def main():
    print("Welcome to the Password Strength Analyzer!")
    password = input("Enter a password to evaluate: ")
    
    result = evaluate_password(password)
    
    print(f"\nPassword Strength: {result['strength']}")
    print(f"Score: {result['score']}/5")
    print("Suggestions:")
    if result['feedback']:
        for suggestion in result['feedback']:
            print(f"- {suggestion}")
    else:
        print("No improvements needed. Your password is strong!")

if __name__ == "__main__":
    main()
