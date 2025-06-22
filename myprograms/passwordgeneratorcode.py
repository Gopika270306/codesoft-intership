import random
import string


def generate_password(username, dob, length):

    if length < 8:
        return "Password must be at least 8 characters long."

    # Take first 2 letters of name and last 4 of DOB
    part1 = username[:2].capitalize()
    part2 = dob[-4:]

    # Create pool of characters
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Generate remaining random characters
    remaining = length - len(part1 + part2)
    random_part = ''
    for i in range(remaining):
        random_part += random.choice(all_chars)

    # Combine all parts
    password = part1 + part2 + random_part

    # Shuffle characters
    password = ''.join(random.sample(password, len(password)))

    return password


# Main program
print("Welcome to the Simple Password Generator!")
name = input("Enter your name: ")
dob = input("Enter your date of birth (DD MM YYYY): ")
length = int(input("Enter password length (minimum 8): "))

result = generate_password(name, dob, length)
print("Generated Password:", result)
