import re

def evaluate_password(password):
    """
    Evaluates the strength of a password and provides feedback.
    Returns a score and improvement suggestions.
    """

    # Criteria and their corresponding scores
    is_length_sufficient = len(password) >= 12
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Common password patterns
    common_patterns = [
        "password", "12345", "qwerty", "abc123", "letmein", "admin", "welcome"
    ]
    common_criteria = any(pattern in password.lower() for pattern in common_patterns)

    # Calculate score
    score = sum([
        is_length_sufficient, has_lowercase, has_uppercase,
        has_digit, has_special_char
    ])
    
    # Feedback
    feedback = []
    if not is_length_sufficient:
        feedback.append("Increase password length to at least 12 characters.")
    if not has_lowercase:
        feedback.append("Add lowercase letters.")
    if not has_uppercase:
        feedback.append("Include uppercase letters.")
    if not has_digit:
        feedback.append("Use at least one numeric digit.")
    if not has_special_char:
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
