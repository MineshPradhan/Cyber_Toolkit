from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def check_strength(password):
    result = zxcvbn(password)
    score = result["score"]

    if score == 3:
        response = "Strong enough password : Score of 3"
    elif score == 4:
        response = "Very strong password : Score of 4"
    else:
        feedback = result.get("feedback", {})
        warning = feedback.get("warning", "No warning")
        suggestions = feedback.get("suggestions", [])

        response = f"Weak Password : Score of {score}"
        response += f"\nWarning: {warning}"
        response += "\nSuggestions:"
        for suggestion in suggestions:
            response += f" {suggestion}"

    return response

def hash_pw(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed

def verify_password(pw_attempt, hashed):
    if bcrypt.checkpw(pw_attempt.encode("utf-8"), hashed):
        return "Password is correct. Access granted!"
    else:
        return "Incorrect password. Access denied ...xxx"

if __name__ == "__main__":
    # Password creation loop
    while True:
        password1 = getpass("Enter a password to check strength: ")
        strength = check_strength(password1)
        print(strength)

        if strength.startswith("Weak"):
            print("Please choose a stronger password.\n")
        else:
            break

    # Hash password
    hashed_password = hash_pw(password1)
    print("\nPassword successfully hashed.")

    # Verify password
    attempt = getpass("Re-enter the password to verify: ")
    print(verify_password(attempt, hashed_password))