import socket
import base64
from Crypto.Cipher import DES

def des_decrypt(encrypted_text, key):
    """ Decrypts text using DES (ECB mode) """
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode().strip()
    return decrypted_text

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5000))
server_socket.listen(1)

print("Server is running and waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Client connected from {addr}")

received_message = conn.recv(1024).decode()
encoded_key = conn.recv(1024).decode()

decoded_key = base64.b64decode(encoded_key)

print("\n[SERVER] Received DES Encrypted Message:", received_message)

decrypted_message = des_decrypt(received_message, decoded_key)

print("[SERVER] Decrypted Message:", decrypted_message)

conn.close()
server_socket.close()