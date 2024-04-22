import json

def load_passwords_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        passwords = file.read().splitlines()
    return passwords

def check_password(user_input, passwords):
    return user_input in passwords

def main():
    # Load passwords
    passwords = load_passwords_from_txt('passwords.txt')

    while True:
        user_input = input("Enter the password: ")

        if check_password(user_input, passwords):
            print("Password is commonly used. Please choose a stronger password.")
        else:
            print("Password is not commonly used. Good to go!")
            break

if __name__ == "__main__":
    main()
