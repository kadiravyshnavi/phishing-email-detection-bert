def analyze_threats(email_text):

    threats = []

    suspicious_words = [
        "urgent",
        "verify",
        "account",
        "password",
        "login",
        "bank",
        "click here",
        "immediately"
    ]

    text = email_text.lower()

    for word in suspicious_words:
        if word in text:
            threats.append(f"Suspicious keyword detected: {word}")

    return threats
