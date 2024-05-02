def load_passwords_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        passwords = file.read().splitlines()
    return passwords

def check_password(user_input, passwords):
    return user_input in passwords
