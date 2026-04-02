from caesar_cipher_hashing import hashing, caesar

def test():
    text = "Hello123"
    key = 4

    hash_value = hashing(text)
    combined = text + hash_value

    encrypted = caesar(combined, key)
    decrypted = caesar(encrypted, -key)

    retrieved_text = decrypted[:len(text)]
    retrieved_hash = decrypted[len(text):]

    assert retrieved_hash == hashing(retrieved_text)
    print("Test passed")

if __name__ == "__main__":
    test()