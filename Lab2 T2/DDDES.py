import base64
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

def generate_key():
    """ Generates a 16-byte key for TripleDES """
    return b"ThisIsASecret123"  # Must be 16 or 24 bytes for 3DES

def triple_des_encrypt(plain_text, key):
    """ Encrypts text using TripleDES (ECB mode) """
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text.encode(), DES3.block_size))
    return base64.b64encode(encrypted_text).decode()

def triple_des_decrypt(encrypted_text, key):
    """ Decrypts text using TripleDES (ECB mode) """
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(base64.b64decode(encrypted_text)), DES3.block_size)
    return decrypted_text.decode()

# Test TripleDES
key = generate_key()
plaintext = "Hello, Triple DES!"

encrypted_text = triple_des_encrypt(plaintext, key)
decrypted_text = triple_des_decrypt(encrypted_text, key)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)