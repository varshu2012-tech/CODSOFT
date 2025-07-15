import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length < 5:
        return "Password length should be at least 4 characters."
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter desired password length (4 or more): "))
            if length < 5:
                print("Length too short. Try again.")
                continue
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter a number.")
        choice = input("\nGenerate another password? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the password generator. Goodbye!")
            break
if __name__ == "__main__":
    main()