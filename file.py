import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii


# Function to create a new file entry
# Encrypt the text before writing to the file
def create_entry(key):
    name = get_file_name()
    filename = name + ".txt"

    print(f"Type your file content for {name} (Enter END on a new line when done.):")
    with open(filename, "w") as file_management_system:
        while True:
            line = input()
            if line == "END":
                break
            encrypted_line = encrypt(line, key)
            file_management_system.write(encrypted_line + "\n")


# Function to append text to an existing file entry
# Encrypt the text before writing to the file
def append_entry(key):
    name = get_file_name()
    filename = name + ".txt"

    with open(filename, "a") as file_management_system:
        print(f"Type your file content for {name} (Enter END on a new line when done.):")
        while True:
            line = input()
            if line == "END":
                break
            encrypted_line = encrypt(line, key)
            file_management_system.write(encrypted_line + "\n")


# Function to read an entry file
def read_entry(key):
    name = get_file_name()
    filename = name + ".txt"

    try:
        with open(filename, "r") as file_management_system:
            for line in file_management_system:
                decrypted_line = decrypt(line.rstrip(), key)
                print(decrypted_line)
    except FileNotFoundError:
        print(f"Could not find file entry for {name}")


def get_file_name():
    name = input("Please enter the file name without white spaces: ")
    return name


# Encrypt function
def encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    cipher_text = binascii.hexlify(cipher.iv + cipher_text_bytes).decode()
    return cipher_text


# Decrypt function
def decrypt(cipher_text, key):
    cipher_text = binascii.unhexlify(cipher_text)
    iv = cipher_text[:16]
    cipher_text = cipher_text[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv = iv)
    plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return plain_text.decode()


def load_passwords_from_txt(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
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

    key = get_random_bytes(16)
    
    print("Welcome to the File Management System!")

    # While loop for operations
    while True:
        print("\nChoose an operation:")
        print("(x) : Exit")
        print("(n) : Create a new file")
        print("(r) : Read a file")
        print("(a) : Append to an existing file")

        choice = input()

        # Check if the user wants to exit
        if choice == 'x':
            # Return from program
            break

        switcher = {
            'n': create_entry,
            'r': read_entry,
            'a': append_entry
        }

        # Get the function from switcher dictionary
        func = switcher.get(choice, lambda: print("ERROR: Invalid input. Choose again."))

        # Execute the function
        func(key)


if __name__ == "__main__":
    main()
