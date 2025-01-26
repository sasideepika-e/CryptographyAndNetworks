#Monoalphabetic Cipher Decryption
key = "ANDREWICKSOHTBFGJLMPQUVXYZ"
cipher_text = "SEEMSEAOMEDSAMHL"
decrypted_text = ""

reverse_key = {key[i]: chr(ord('A') + i) for i in range(len(key))}

for char in cipher_text:
    decrypted_text += reverse_key[char]

print("Decrypted Text:", decrypted_text)