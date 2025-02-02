import socket
from Lab1.Q7 import playfair_encrypt  

def encrypt(plain_text, key):
    """ Vigenère Cipher Encryption (Same as Java Logic) """
    cipher_text = []
    plain_text = plain_text.upper()
    key = key.upper()

    key_index = 0
    for c in plain_text:
        if 'A' <= c <= 'Z':
            k = key[key_index]
            encrypted_char = chr(((ord(c) - ord('A') + (ord(k) - ord('A'))) % 26) + ord('A'))
            cipher_text.append(encrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            cipher_text.append(c)

    return "".join(cipher_text)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5000))
print("Connected to the server.")

original_message = "wearediscoveredsaveyourself"
plain_text = original_message.lower().replace('j', 'i').replace(" ", "")
key = "deceptive"

encrypted_message = encrypt(original_message, key)

key_matrix = [
    ['s', 'r', 'm', 'a', 'p'],
    ['u', 'n', 'i', 'v', 'e'],
    ['t', 'y', 'b', 'c', 'd'],
    ['f', 'g', 'h', 'k', 'l'],
    ['o', 'q', 'w', 'x', 'z']
]

playfair_encrypted = playfair_encrypt(plain_text, key_matrix)

client_socket.send(encrypted_message.encode())
client_socket.send(playfair_encrypted.encode())

print("\n[CLIENT] Original Message sent to server:", original_message)
print("[CLIENT] Cipher Message sent to server:", encrypted_message)
print("[CLIENT] Playfair Encrypted Message sent to server:", playfair_encrypted)

client_socket.close()