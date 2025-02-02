import socket
import base64
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad(text):
    """ Pads text to ensure it's a multiple of 8 bytes (64 bits). """
    while len(text) % 8 != 0:
        text += " "
    return text

def generate_key():
    """ Generates a DES key (8 bytes) """
    return get_random_bytes(8)

def des_encrypt(plain_text, key):
    """ Encrypts text using DES (ECB mode) """
    cipher = DES.new(key, DES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode())
    return base64.b64encode(encrypted_text).decode()

server_ip = "localhost"
server_port = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print("Connected to the server.")

secret_key = generate_key()
encoded_key = base64.b64encode(secret_key).decode()

original_message = "SasiDeepika"
encrypted_message = des_encrypt(original_message, secret_key)

client_socket.send(encrypted_message.encode())
client_socket.send(encoded_key.encode())

print("\n[CLIENT] Original Message sent to server:", original_message)
print("[CLIENT] DES Encrypted Message sent to server:", encrypted_message)

client_socket.close()