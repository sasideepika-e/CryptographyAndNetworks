#Caesar Cipher Decryption with All Keys
cipher_text = "PHHW PH DIWHU WKH WRJD SDUWB"

for key in range(1, 27):
    decrypted = ""
    for char in cipher_text:
        if char.isalpha():
            decrypted += chr(((ord(char) - ord('A') - key + 26) % 26) + ord('A'))
        else:
            decrypted += char
    print(f"Key {key}: {decrypted}")