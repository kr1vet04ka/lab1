def xor_cipher(text: str, key: str) -> str:
    """
    Виконує шифрування або розшифрування тексту за допомогою XOR-шифру.
    """
    encrypted = []
    for i in range(len(text)):
        encrypted_char = chr(ord(text[i]) ^ ord(key[i % len(key)]))
        encrypted.append(encrypted_char)
    return "".join(encrypted)