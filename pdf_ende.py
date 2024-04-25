from PyPDF2 import PdfWriter, PdfReader 

def pdf_encrypt(filepath, passwd):
    reader = PdfReader(filepath)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(passwd)
    with open(filepath, "wb") as f:
        writer.write(f)

def pdf_decrypt(filepath, passwd):
    reader = PdfReader(filepath)
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt(passwd)

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Save the new PDF to a file
    with open(filepath, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    passwd = input("Enter the password for the pdf file: ")
    filepath = input("Enter the absolute path of the pdf file: ") #check the input?
    pdf_encrypt(filepath, passwd)
    pdf_decrypt(filepath, passwd)
