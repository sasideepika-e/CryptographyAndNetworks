#Vigenere Cipher Encryption and Decryption
def encrypt(text, key):
    result = ""
    j = 0
    for char in text:
        result += chr(((ord(char) - ord('a') + ord(key[j]) - ord('a')) % 26) + ord('a'))
        j = (j + 1) % len(key)
    return result

def decrypt(text, key):
    result = ""
    j = 0
    for char in text:
        result += chr(((ord(char) - ord('a') - (ord(key[j]) - ord('a')) + 26) % 26) + ord('a'))
        j = (j + 1) % len(key)
    return result

plain_text = "wearediscoveredsaveyourself"
key = "deceptive"
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)
print("Encrypted Message:", encrypted_text)
print("Decrypted Message:", decrypted_text)