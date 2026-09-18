from lib import xor_cipher

def main():
    secret_message = "ConfidentialData"
    encryption_key = "secure"

    print("--- Тестування XOR шифрування ---")
    print(f"Оригінальне повідомлення: {secret_message}")

    encrypted_msg = xor_cipher(secret_message, encryption_key)
    print(f"Зашифрований текст: {repr(encrypted_msg)}")

    decrypted_msg = xor_cipher(encrypted_msg, encryption_key)
    print(f"Розшифрований текст: {decrypted_msg}")

if __name__ == "__main__":
    main()