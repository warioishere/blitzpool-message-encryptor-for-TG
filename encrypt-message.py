#!/usr/bin/env python3

import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# Der Public Key als PEM-String (wie bei dir angegeben)
PUBLIC_KEY_PEM = b"""-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAr/zLq5zMc9Ty8uYwbvjH
Hkkh3Kz9URqaORJOnwd+1I75t2fFMRnwORjfFiF/3jdYfTHbtKD1sO4t0f0jmwnv
2yO0A+9mgyl+LrjWDyFmofGJcrJy7+J895Jm7fjoR84G93A3uAYI0PyrNmGngyNI
V7LiPTNT1iCvXjCUGD9r0m9OGawql1EQ9OinbzyFo6m+cpbj+3lJHtN2VmpaTYkS
lblS85pDrrJjnpXtHThSdKRCsheJoWRDA+I0eCmqsfTINSV0sOrGTF64yzzRR/Km
o8oQdBVuXdzZR5L3LZEZjUhUh/8b35WV2fp0yR581XtoLwrMPCb9whx2UQMAbDZR
E8l/zoQUP3StcP6gto9NFGOHRowfrH3CFcVw4qfl+paeniSDy0bbvZH9WwWA7BJ3
rqPGORxZ9dohGsQ150RLdWq8QtWu+cjjC38hlkiQnq+YhJM5/CtiP7WZTjcqLhgn
c3hOcx/G2nXx/zNYs8MQbDIYR7w6IsdVGbDGU1/WGibUkPVs7GAPq//ujKYyehu5
sDLLUEx9CLfi2UHn9NTmRp3J6arFjJKZsNUy5bF0JLECzruXKVvYIgtrpN3PixS+
6CtjDlnDtjLo+2Ozt4S1kLui+aMmcErJJfa/j/E0EMsL4hiM3OFDDoM6EwiEPmDP
J6xsgaNaEHS49GQMz4TA4LMCAwEAAQ==
-----END PUBLIC KEY-----"""

def load_public_key():
    return serialization.load_pem_public_key(PUBLIC_KEY_PEM, backend=default_backend())

def encrypt_message(public_key, message):
    ciphertext = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode('utf-8')

def main():
    print("Willkommen zum Verschlüsselungstool für den BlitzPool Bot 🔒\n")
    public_key = load_public_key()

    message = input("Gib deine Nachricht ein (z.B. /subscribe 1BitcoinAdresse...):\n> ").strip()
    if not message:
        print("❗️ Nachricht darf nicht leer sein.")
        return

    encrypted = encrypt_message(public_key, message)

    print("\nHier ist deine verschlüsselte Nachricht (sende sie an den Bot):\n")
    print(encrypted)

if __name__ == "__main__":
    main()
