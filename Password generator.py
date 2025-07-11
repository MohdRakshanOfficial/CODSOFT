import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 characters for better security."

    # Character sets
    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&*()_+ etc.

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure at least one from each category
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random choices from all characters
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the result to avoid fixed pattern
    random.shuffle(password)

    return ''.join(password)

# Input from user
length = int(input("Enter desired password length: "))
secure_password = generate_password(length)
print("Generated Password:", secure_password)
