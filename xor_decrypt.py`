#!/usr/bin/env python3
from BitVector import BitVector

# Read key
with open("key.bin", "rb") as f:
    key_raw = f.read()
key = BitVector(rawbytes=key_raw)

# Read ciphertext
with open("cipher.hex", "r") as f:
    cipher_hex = f.read()
cipher = BitVector(hexstring=cipher_hex)

# Decrypt
data = cipher ^ key

# Choose output method:
print(data.get_text_from_bitvector())                    # Option 1: print to console

# with open("decrypted.txt", "w") as f:                  # Option 2: save to file
#     f.write(data.get_text_from_bitvector())
