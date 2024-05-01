def image_encrypt(key):
    try:
        path = input(r'Enter path of Image : ')

        # open file for reading purpose
        fin = open(path, 'rb')

        # Store image data in variable "image"
        image = fin.read()
        fin.close()

        # Check if the image has already been encrypted
        marker = b'ENCRYPTED'
        if image[-len(marker):] == marker:
            print('Image already encrypted.')
            return

        # converting image into byte array to perform encryption on numeric data
        image = bytearray(image)

        # Convert key to an integer
        key_int = int.from_bytes(key, 'big')

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ (key_int % 256)

        # Add the marker to the end of the image data
        image += marker

        # open file for writing purpose & write encrypted data in image
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()

        # Save the key to a file
        with open(path + '.key', 'w') as key_file:
            key_file.write(str(key_int))

        print('Encryption Done...')

    except FileNotFoundError:
        print('File not found...')
        
    except Exception as e:
        print('An error occurred:', str(e))


def image_decrypt(key):
    try:
        path = input(r'Enter path of Image : ')
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()

        marker = b'ENCRYPTED'
        if image[-len(marker):] != marker:
            print('Image not encrypted.')
            return

        image = image[:-len(marker)]
        image = bytearray(image)

        # Retrieve key from the saved file
        key_file_path = path + '.key'
        with open(key_file_path, 'r') as key_file:
            key_int = int(key_file.read())

        for index, values in enumerate(image):
            image[index] = values ^ (key_int % 256)

        if b'ENCRYPTED' in image:
            raise ValueError('Decryption failed. Wrong key.')

        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Decryption Done...')

    except FileNotFoundError:
        print('File not found...')
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print('An error occurred:', str(e))
