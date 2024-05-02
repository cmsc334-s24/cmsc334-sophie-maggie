## Security Final Project

**Authors: Sophie Zhao, Maggie Song**

#### Introduction

Individuals and organizations are increasingly vulnerable to data breaches and unauthorized access. Therefore, there is a critical need for robust tools that enhance the security of sensitive files and data management practices. We plan to address this problem with the following application, helping users to secure their files by encrypting and decrypting a diverse range of file types including text documents, PDFs, images, audios, and videos. Our application also includes a comprehensive password check to ensure the password set up by the user is strong enough and thus enhance protection against unauthorized access.


#### Technologies Used

We use Python to develop this application and use libraries such as pycryptodome, PyPDF, and cryptography for some specific file type encryption and decryption. 


#### Implementation Details

There are four main approaches we have employed to handle different file types:

1. Salt：We incorporate a salt into users' passwords as an additional input to the encryption process. This enhances security by making it more challenging for attackers to deduce the encryption key through brute force attacks. It operates in conjunction with the SHA-256 hashing algorithm to generate a key.

2. AES and CBC: For the text document, we use Advanced Encryption Standard (AES) with Cipher Block Chaining (CBC) mode for encryption and decryption. It initializes an AES cipher in CBC mode with the provided key. The plaintext is padded to ensure its length is a multiple of the AES block size. The encrypt method is called on the AES cipher object to encrypt the padded plaintext. The initialization vector and the resulting ciphertext are combined and converted to hexadecimal format using binascii.hexlify.

3. PyPDF2: PyPDF2 is a Python library for working with PDF files. It reads the PDF file using PdfReader from PyPDF2, then it checks if the PDF is already encrypted using the is_encrypted attribute of the PdfReader object. If it is already encrypted, it prints a message and returns. Otherwise, it initializes a PdfWriter object and adds all pages from the PdfReader object to it. It encrypts the PDF using the provided key using the encrypt method of the PdfWriter object, and finally, it writes the encrypted PDF to the original file path.

4. Fernet: Fernet is a symmetric encryption algorithm introduced in the cryptography library in Python. In the derive_key_from_password function, a helper function takes a password as input and derives a Fernet key from it using PBKDF2HMAC algorithm with SHA256 hashing. It generates a salt, applies PBKDF2HMAC with 100,000 iterations, and derives a 32-byte key. Finally, it converts the key to a URL-safe base64-encoded string and returns it. There is also another function to check if a file has the .encrypted extension, to make sure we don't encrypt the same file twice.


#### Code Structure

We have a main file to drive the execution. Additionally, we have three separate files for text documents, PDFs, and multimedia (such as images, audio, and video), each with a different encryption and decryption technique corresponding to its file type. In parallel, we also have a password check file and a common password repository to verify against any common passwords.

The common password repository is a file containing the top 100,000 passwords from the **Have I Been Pwned (https://haveibeenpwned.com)** data set by Troy Hunt, sponsored by the National Cyber Security Center. This is a very interesting dataset/website, people can also check if their email addresses are in a data breach or not. It also offers an API service, so developers could make use of an external service.


#### How to Run

To run this application, users will need to:

1. Set up a virtual environment and then run `pip3 install -r requirements.txt`, which contains all the necessary packages.

2. Next, run `python3 main.py` to execute the application.


#### Future Improvements

The current application is designed for individual users, restricting access to documents to only the user. If someone steals your computer, they cannot access the encrypted data without the correct passwords.

To enhance accessibility and usability, we can transform it into a web application.


#### Conclusion

In this project, we have developed a secure file management system that enables users to encrypt and decrypt various file types, ensuring the confidentiality of their data. By incorporating encryption methods and password protection, we ensure that even if a user's device is compromised, their data can remain secure.

Learning how to implement various encryption techniques and integrate them into a functional application has provided us valuable insights into cryptography and cybersecurity.


#### Citation

https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt 

https://www.ncsc.gov.uk/blog-post/passwords-passwords-everywhere

https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html#

https://cryptography.io/en/latest/fernet/


