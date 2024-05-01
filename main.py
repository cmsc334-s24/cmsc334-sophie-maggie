import os
import hashlib
from text_ende import create_entry, append_entry, read_entry
from image_ende import image_encrypt, image_decrypt
from pdf_ende import pdf_encrypt, pdf_decrypt

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
        user_input = input("Enter your password: ")

        if check_password(user_input, passwords):
            print("Password is commonly used. Please choose a stronger password.")
        else:
            print("Password is not commonly used. Good to go!")
            break

    salt = b'totalrandomsalt' 
    key = hashlib.pbkdf2_hmac('sha256', user_input.encode(), salt, 100000)  
    key = key[:16]

    print("Welcome to the File Management System!")

    # Check if the key file exists
    if os.path.exists('key.bin'):
        # Read the key from the file
        with open('key.bin', 'rb') as key_file:
            key = key_file.read()

    # While loop for operations
    while True:
        print("")
        print("What type of file would you like to manage?")
        print("1. Text file")
        print("2. Image file")
        print("3. PDF file")
        print("4. Audio file")
        print("5. Exit")
        filetype = input("Enter the number of the file type you would like to manage:")
        
        if filetype == "1":
            print("\nChoose an operation:")
            print("(x) : Return to main menu")
            print("(n) : Create a new text file")
            print("(r) : Read a text file")
            print("(a) : Append to an existing text file")
            choice = input()
            if choice == 'x':
                continue
            elif choice == 'n':
                create_entry(key)
            elif choice == 'r':
                read_entry(key)
            elif choice == 'a':
                append_entry(key)
            else:
                print("ERROR: Invalid input. Choose again.")
        
        elif filetype == "2":
            print("\nChoose an operation:")
            print("(x) : Return to main menu")
            print("(e) : Encrypt an image file")
            print("(d) : Decrypt an image file")
            choice = input()
            if choice == 'x':
                continue
            elif choice == 'e':
                image_encrypt(key)
            elif choice == 'd':
                image_decrypt(key)
            else:
                print("ERROR: Invalid input. Choose again.")
       
        elif filetype == "3":
            print("\nChoose an operation:")
            print("(x) : Return to main menu")
            print("(e) : Encrypt a PDF file")
            print("(d) : Decrypt a PDF file")
            choice = input()
            if choice == 'x':
                continue
            elif choice == 'e':
                pdf_encrypt(user_input)
            elif choice == 'd':
                pdf_decrypt(user_input)
            else:
                print("ERROR: Invalid input. Choose again.")
        
        elif filetype == "4":
            print("\nChoose an operation:")
            print("(x) : Return to main menu")
            print("(e) : Encrypt an audio file")
            print("(d) : Decrypt an audio file")
            choice = input()
            if choice == 'x':
                continue
            elif choice == 'e':
                print("Audio file management is not supported in this version.")
            elif choice == 'd':
                print("Audio file management is not supported in this version.")
            else:
                print("Audio file management is not supported in this version.")
        
        elif filetype == "5":
            print("Exiting the File Management System. Goodbye!")
            break

if __name__ == "__main__":
    main()
