# CMSC 334: Computer Security Final Project
# @authors: Sophie Zhao & Maggie Song
import hashlib
from passwd_check import load_passwords_from_txt, check_password
from text_ende import create_entry, append_entry, read_entry
from pdf_ende import pdf_encrypt, pdf_decrypt
from multimedia_ende import multimedia_encrypt, multimedia_decrypt

def main():
    # Load passwords
    passwords = load_passwords_from_txt('passwords.txt')

    # Prompt user to enter password
    while True:
        user_input = input("Enter your password: ")
        if len(user_input) <= 4:
            print("Password is too short. The length of the password should be greater than 4.")

        if check_password(user_input, passwords):
            print("Password is commonly used. Please choose a stronger password.")
        else:
            print("Password is not commonly used. Good to go! \n")
            break
    
    # Derive the key for the text encryption & decryption from the user typed password
    salt = b'totalrandomsalt' 
    key = hashlib.pbkdf2_hmac('sha256', user_input.encode(), salt, 100000)  
    key = key[:16]
    
    print("Welcome to the File Management System!")

    # While loop for operations
    while True:
        print("")
        print("What type of file would you like to manage?")
        print("1. Text file")
        print("2. PDF file")
        print("3. Image/Audio/Video file")
        print("4. Exit")
        filetype = input("Enter the number of the file type you would like to manage: ")
        if filetype == "1":
            print("\nChoose an operation:")
            print("(x) : Return to main menu")
            print("(n) : Create a new text file")
            print("(r) : Read a text file")
            print("(a) : Append to an existing text file")
            choice = input()
            while choice not in ['x', 'n', 'r', 'a']:
                print("ERROR: Invalid input. Choose again.")
                choice = input()
            if choice == 'x':
                continue
            elif choice == 'n':
                create_entry(key)
            elif choice == 'r':
                read_entry(key)
            elif choice == 'a':
                append_entry(key)
        elif filetype == "2":
            print("\nChoose an operation:")
            print("(x) : Return to main menu")
            print("(e) : Encrypt a PDF file")
            print("(d) : Decrypt a PDF file")
            choice = input()
            while choice not in ['x', 'e', 'd']:
                print("ERROR: Invalid input. Choose again.")
                choice = input()
            if choice == 'x':
                continue
            elif choice == 'e':
                pdf_encrypt(user_input)
            elif choice == 'd':
                pdf_decrypt(user_input)
        elif filetype == "3":
            print("\nChoose an operation:")
            print("(x) : Return to main menu")
            print("(e) : Encrypt an image/audio/video file")
            print("(d) : Decrypt an image/audio/video file")
            choice = input()
            while choice not in ['x', 'e', 'd']:
                print("ERROR: Invalid input. Choose again.")
                choice = input()
            if choice == 'x':
                continue
            elif choice == 'e':
                multimedia_encrypt(user_input)
            elif choice == 'd':
                multimedia_decrypt(user_input)
        elif filetype == "4":
            print("Exiting the File Management System. Goodbye!")
            break

if __name__ == "__main__":
    main()
