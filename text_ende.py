import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

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
    try:
        plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
    except ValueError:
        return "Password incorrect, please log out and try again."
    return plain_text.decode()
