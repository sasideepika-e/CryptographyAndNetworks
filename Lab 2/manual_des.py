import itertools

# Permutation tables (same as Java version)
PERM_ARRAY = [15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9,
              1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24]

EXP_ARRAY = [31, 0, 1, 2, 3, 4, 3, 4,
             5, 6, 7, 8, 7, 8, 9, 10,
             11, 12, 11, 12, 13, 14, 15, 16,
             15, 16, 17, 18, 19, 20, 19, 20,
             21, 22, 23, 24, 23, 24, 25, 26,
             27, 28, 27, 28, 29, 30, 31, 0]

PC1_ARRAY = [56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26,
             18, 10, 2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29,
             21, 13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]

PC2_ARRAY = [13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3, 25, 7,
             15, 6, 26, 19, 12, 1, 40, 51, 30, 36, 46, 54, 29, 39, 50, 44, 32,
             47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35, 28, 31]

SBOX = [
    ["0010", "0100", "0010", "1001", "1011", "1111", "1011", "1111",
     "1111", "1010", "1010", "0100", "0110", "1101", "0110", "0001"]
] * 4  # Using Java S-Box structure

def permutate(input_str, table):
    return ''.join(input_str[i] for i in table)

def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))

def left_circular_shift(bits, shifts=1):
    return bits[shifts:] + bits[:shifts]

def sbox_substitution(input_str):
    output = ""
    for i in range(0, len(input_str), 6):
        row = int(input_str[i] + input_str[i+5], 2)
        col = int(input_str[i+1:i+5], 2)
        output += SBOX[row][col]
    return output

def feistel_function(right, key):
    expanded = permutate(right, EXP_ARRAY)
    xored = xor(expanded, key)
    substituted = sbox_substitution(xored)
    return permutate(substituted, PERM_ARRAY)

def generate_round_keys(key):
    round_keys = []
    pc1_key = permutate(key, PC1_ARRAY)
    left_key, right_key = pc1_key[:28], pc1_key[28:]

    for round_num in range(16):
        shifts = 1 if round_num in [0, 1, 8, 15] else 2
        left_key = left_circular_shift(left_key, shifts)
        right_key = left_circular_shift(right_key, shifts)
        combined_key = left_key + right_key
        round_keys.append(permutate(combined_key, PC2_ARRAY))

    return round_keys

def text_to_binary(text):
    binary = ''.join(format(ord(c), '08b') for c in text)
    return binary.ljust(64, '0')  # Ensure 64-bit block

def binary_to_text(binary):
    """ Converts binary string back to text while ensuring full 64-bit recovery """
    binary = binary[:64]  # Force 64-bit length
    chars = [chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars).rstrip('\x00')

def des_encrypt(plaintext, key):
    round_keys = generate_round_keys(key)
    binary_text = text_to_binary(plaintext)

    left, right = binary_text[:32], binary_text[32:]

    for round_key in round_keys:
        temp = right
        right = xor(left, feistel_function(right, round_key))
        left = temp

    return right + left  # Final swap

def des_decrypt(ciphertext, key):
    round_keys = generate_round_keys(key)
    left, right = ciphertext[:32], ciphertext[32:]

    for round_key in reversed(round_keys):
        temp = right
        right = xor(left, feistel_function(right, round_key))
        left = temp

    return binary_to_text(right + left)

# Main Execution
plaintext = "Sasi"
key = "eluri123"  # 64-bit key equivalent
binary_key = text_to_binary(key)[:64]

encrypted = des_encrypt(plaintext, binary_key)
decrypted = des_decrypt(encrypted, binary_key)

print("Original Text:", plaintext)
print("Encrypted Binary:", encrypted)
print("Decrypted Binary:", text_to_binary(decrypted))  # Debugging output
print("Decrypted Text:", decrypted)