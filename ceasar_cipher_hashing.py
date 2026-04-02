def hashing(text, length=12):
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p = 31
    m = 2305843009213693951
    hash_value = 0
    p_pow = 1
    
    for ch in text:
        hash_value = (hash_value + ord(ch) * p_pow) % m
        p_pow = (p_pow * p) % m
        
    result = []
    
    if hash_value == 0:
        return chars[0] * length

    while hash_value > 0:
        hash_value, remainder = divmod(hash_value, 62)
        result.append(chars[remainder])
    
    hash_str = "".join(result[::-1])
    
    if len(hash_str) < length:
        return hash_str.ljust(length, '0')
    return hash_str[:length]


def caesar(text, key):
    result = ''
    for ch in text:
        if ch.isdigit():
            result += chr(((ord(ch) - ord('0') + key) % 10) + ord('0'))
        elif ch.islower():
            result += chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
        elif ch.isupper():
            result += chr(((ord(ch) - ord('A') + key) % 26) + ord('A'))
        else:
            result += ch
    return result


# Main Execution
plain_text = input("Enter Plain Text: ")
key = int(input("Enter shift key: "))

# Generate hash
hash_value = hashing(plain_text)

# Append hash to plaintext
combined_text = plain_text + hash_value
print("Plain + Hash:", combined_text)

# Encrypt
encrypted_text = caesar(combined_text, key)
print("Encrypted Text:", encrypted_text)

# Decrypt
decrypted_text = caesar(encrypted_text, -key)

# Separate original text and hash
retrieved_text = decrypted_text[:len(plain_text)]
retrieved_hash = decrypted_text[len(plain_text):]

print("Decrypted Text:", retrieved_text)
print("Retrieved Hash:", retrieved_hash)

# Verify integrity
if retrieved_hash == hashing(retrieved_text):
    print("Integrity Verified: No tampering detected")
else:
    print("Data integrity check failed")