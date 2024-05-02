# Perform PDF encryption and decryption using PyPDF2 library.
from PyPDF2 import PdfWriter, PdfReader

def pdf_encrypt(passwd):
    try:
        filepath = input('Enter the absolute path of the pdf: ')
        reader = PdfReader(filepath)
        writer = PdfWriter()

        # check if the pdf is encrypted
        if reader.is_encrypted:
            print("PDF is already encrypted.")
            return
        # add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)
        # encrypt the pdf with provided password
        writer.encrypt(passwd)
        with open(filepath, "wb") as f:
            writer.write(f)
        print("PDF encrypted successfully.")
    
    except FileNotFoundError:
        print('File not found...')

def pdf_decrypt(passwd):
    try:
        filepath = input('Enter the absolute path of the PDF: ')
        reader = PdfReader(filepath)
        writer = PdfWriter()
        # check if the PDF is encrypted
        if reader.is_encrypted:
            # decrypt the pdf with provided password
            if reader.decrypt(passwd):
                # add all pages to the writer
                for page in reader.pages:
                    writer.add_page(page)
                # save the new PDF to a file
                with open(filepath, "wb") as f:
                    writer.write(f)
                print("PDF decrypted successfully.")
            else:
                print("Incorrect password.")
        else:
            print("PDF is not encrypted or has already been decrypted.")

    except FileNotFoundError:
        print('File not found...')
