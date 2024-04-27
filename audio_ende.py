from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import wave

def audio_encrypt(input_file, output_file, key):
    # Read audio data
    with wave.open(input_file, 'rb') as wav:
        audio_data = wav.readframes(wav.getnframes())

    # Encrypt audio data
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(audio_data)

    # Write encrypted data to output file
    with open(output_file, 'wb') as f:
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)

def audio_decrypt(input_file, output_file, key):
    # Read encrypted data
    with open(input_file, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    # Decrypt data
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

    # Write decrypted audio data to output file
    with wave.open(output_file, 'wb') as wav:
        wav.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))
        wav.writeframes(decrypted_data)

# Example usage:
input_audio_file = 'input_audio.wav'
output_encrypted_file = 'encrypted_audio.enc'
output_decrypted_file = 'decrypted_audio.wav'
encryption_key = get_random_bytes(16)  # 16 bytes key for AES-128
print(encryption_key)

# # Encrypt the audio file
# audio_encrypt(input_audio_file, output_encrypted_file, encryption_key)

# # Decrypt the encrypted audio file
# audio_decrypt(output_encrypted_file, output_decrypted_file, encryption_key)
