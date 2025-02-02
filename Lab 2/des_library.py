from Crypto.Cipher import DES
import base64

def pad(text):
    """ Pads text to ensure it's a multiple of 8 bytes (64 bits). """
    while len(text) % 8 != 0:
        text += " "
    return text

def des_encrypt(text, key):
    """ Encrypts the given text using DES with ECB mode. """
    key = key[:8].encode()  # Ensure 8-byte key
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(text).encode())
    return base64.b64encode(encrypted_text).decode()

def des_decrypt(encrypted_text, key):
    """ Decrypts the given Base64 encoded DES encrypted text. """
    key = key[:8].encode()  # Ensure 8-byte key
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode().strip()
    return decrypted_text

# Main Execution
plaintext = "Sasi"
key = "eluri123"  # 8-byte key required for DES

encrypted_text = des_encrypt(plaintext, key)
decrypted_text = des_decrypt(encrypted_text, key)

print("Original Text:", plaintext)
print("Encrypted (Base64 Encoded):", encrypted_text)
print("Decrypted Text:", decrypted_text)
