import requests

def download_dataset(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

dataset_url = 'https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt'
dataset_file_path = 'passwords.txt'
download_dataset(dataset_url, dataset_file_path)
