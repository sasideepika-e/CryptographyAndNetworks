import socket
import struct
from Lab1.Q8 import playfair_decrypt

def decrypt(cipher_text, key):
    """ Vigenère Cipher Decryption (Same as Java Logic) """
    plain_text = []
    cipher_text = cipher_text.upper()
    key = key.upper()

    key_index = 0
    for c in cipher_text:
        if 'A' <= c <= 'Z':
            k = key[key_index]
            decrypted_char = chr(((ord(c) - ord(k) + 26) % 26) + ord('A'))
            plain_text.append(decrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            plain_text.append(c)

    return "".join(plain_text)

# Server Setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5000))
server_socket.listen(1)

print("Server is running and waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Client connected from {addr}")

received_message = conn.recv(1024).decode()
print("CIPHER from client:", received_message)

received_message_playfair = conn.recv(1024).decode()
print("Playfair from client:", received_message_playfair)

key = "deceptive"
decrypted_message = decrypt(received_message, key)
print("Hello, client! Your Caesar message was:", decrypted_message)

key_matrix = [
    ['s', 'r', 'm', 'a', 'p'],
    ['u', 'n', 'i', 'v', 'e'],
    ['t', 'y', 'b', 'c', 'd'],
    ['f', 'g', 'h', 'k', 'l'],
    ['o', 'q', 'w', 'x', 'z']
]

playfair_decrypted = playfair_decrypt(received_message_playfair, key_matrix)
print("Hello, client! Your Playfair message was:", playfair_decrypted)

conn.close()
server_socket.close()