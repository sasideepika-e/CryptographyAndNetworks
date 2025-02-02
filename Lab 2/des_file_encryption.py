from Crypto.Cipher import DES
import base64

def pad(text):
    while len(text) % 8 != 0:
        text += " "
    return text

def des_encrypt_file(input_file, output_file, key):
    key = key[:8].encode()
    cipher = DES.new(key, DES.MODE_ECB)

    with open(input_file, "r") as file:
        plaintext = file.read()
    
    encrypted_text = cipher.encrypt(pad(plaintext).encode())
    with open(output_file, "wb") as file:
        file.write(base64.b64encode(encrypted_text))

def des_decrypt_file(input_file, output_file, key):
    key = key[:8].encode()
    cipher = DES.new(key, DES.MODE_ECB)

    with open(input_file, "rb") as file:
        encrypted_text = base64.b64decode(file.read())
    
    decrypted_text = cipher.decrypt(encrypted_text).decode().strip()
    with open(output_file, "w") as file:
        file.write(decrypted_text)

# File Paths
original_file = "original.txt"
encrypted_file = "encrypted.txt"
decrypted_file = "decrypted.txt"

# Sample Text
with open(original_file, "w") as file:
    file.write("Hello, this is Sasi Deepika!")

key = "eluri123"  # 8-byte key

# Encrypt File
des_encrypt_file(original_file, encrypted_file, key)

# Decrypt File
des_decrypt_file(encrypted_file, decrypted_file, key)

print("File encryption and decryption completed. Check the files.")