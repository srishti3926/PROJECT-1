
import random
import string

def generate_password(length):
    # Define all possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password by randomly choosing characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    try:
        # Prompt user for password length
        length = int(input("Enter desired password length: "))
        
        # Validate length
        if length < 4:
            print("Password should be at least 4 characters long.")
        else:
            # Generate and display password
            password = generate_password(length)
            print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the program
main()
