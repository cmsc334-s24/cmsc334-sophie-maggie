def image_encrypt():
	try:
		# take path of image as a input
		path = input(r'Enter path of Image : ')

		# open file for reading purpose
		fin = open(path, 'rb')
		
		# storing image data in variable "image"
		image = fin.read()
		fin.close()
		
		# converting image into byte array to perform encryption on numeric data
		image = bytearray(image)

		# taking encryption key as input
		while True:
			try:
				key = int(input('Enter an integer (from 0 to 255) as a key for encryption of Image: '))
				break
			except ValueError:
				print('Please enter a valid integer key...')

		# performing XOR operation on each value of bytearray
		for index, values in enumerate(image):
			image[index] = values ^ key

		# open file for writing purpose & write encrypted data in image
		fin = open(path, 'wb')
		fin.write(image)
		fin.close()
		print('Encryption Done...')
	except FileNotFoundError:
		print('File not found...')


def image_decrypt():
	try:
		# take path of image as a input
		path = input(r'Enter path of Image : ')
		fin = open(path, 'rb')
		image = fin.read()
		fin.close()
		# taking encryption key as input
		while True:
			try:
				key = int(input('Enter an integer as a key for encryption of Image: '))
				break
			except ValueError:
				print('Please enter a valid integer key...')
		
		image = bytearray(image)
		for index, values in enumerate(image):
			image[index] = values ^ key
		fin = open(path, 'wb')
		fin.write(image)
		fin.close()
		print('Decryption Done...')
	except FileNotFoundError:
		print('File not found...')
	