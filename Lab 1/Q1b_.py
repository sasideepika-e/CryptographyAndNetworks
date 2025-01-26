#Simple Encryption (Caesar Cipher)
def encrypt(text, key):
    result = ""
    for char in text:
        result += chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
    return result

plain_text = "computerscienceengineeringsrmuniversity"
key = 4
encrypted_text = encrypt(plain_text, key)
print("Encrypted Message:", encrypted_text)