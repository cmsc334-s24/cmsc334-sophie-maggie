from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

# helper function: convert the password to a Fernet key
def derive_key_from_password(password):
    password_bytes = password.encode()
    salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32, 
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password_bytes)
    return base64.urlsafe_b64encode(key) # convert key to base64-encoded URL-safe string

# helpful function: check if a file has the .encrypted extension
def is_encrypted(path):
    filename, extension = os.path.splitext(path)
    return extension == '.encrypted'

def multimedia_encrypt(password):
    try:
        # take path of audio file as a input
        path = input(r'Enter path of Audio file : ')

        # Check if file is already encrypted
        if is_encrypted(path):
            print("File is already encrypted.")
            return
        
        # open the file and read it
        fin = open(path, 'rb')
        audio = fin.read()
        fin.close()

        # get the key from the password and creqte a cipher suite to perform encryption
        key = derive_key_from_password(password)
        cipher_suite = Fernet(key)
        encrypted_audio = cipher_suite.encrypt(audio)

        # open the file in write binary mode and write the encrypted file
        fin = open(path + '.encrypted', 'wb')
        fin.write(encrypted_audio)
        fin.close()
        print('Encryption Done...')

        # Ask user if they want to delete the original file
        user_input = input("Do you want to delete the original file? (y/n): ")
        while user_input.lower() not in ['y', 'n']:
            print('Invalid input. Please enter y or n.')
            user_input = input("Do you want to delete the original file? (y/n): ")
        if user_input.lower() == 'y':
            os.remove(path)
            print('Original file deleted.')
        elif user_input.lower() == 'n':
            print('Original file not deleted.')
    
    except FileNotFoundError:
        print('File not found...')

def multimedia_decrypt(password):
    try:
        path = input(r'Enter path of Audio file : ')
        
        fin = open(path, 'rb')
        # Check if file is encrypted
        if not is_encrypted(path):
            print("File is not encrypted.")
            return
        audio = fin.read()
        fin.close()

        key = derive_key_from_password(password)

        # Validate key format
        try:
            cipher_suite = Fernet(key)
        except ValueError:
            print('Invalid key format. Key must be 32 url-safe base64-encoded bytes.')
            return

        try:
            # Decrypt the file and write the decrypted file
            decrypted_audio = cipher_suite.decrypt(audio)
            fin = open(path.replace('.encrypted', ''), 'wb')
            fin.write(decrypted_audio)
            fin.close()
            print('Decryption Done...')

            # Delete the encrypted file
            os.remove(path)
            print('Encrypted file deleted.')

        except InvalidToken:
            print('Wrong key provided... Decryption failed.')

    except FileNotFoundError:
        print('File not found...')
