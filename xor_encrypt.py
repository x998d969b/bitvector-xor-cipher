#!/usr/bin/env python3
from BitVector import BitVector
import secrets

# Choose one option:
# data = BitVector(textstring="YOUR TEXT HERE")         # Option 1: encrypt text
data = BitVector(rawbytes=open("NON.txt", "rb").read())  # Option 2: encrypt file

block_size = 128
remainder = data.length() % block_size
if remainder != 0:
    padding = block_size - remainder
    data.pad_from_right(padding)

data_bytes = data.length() // 8
key_bytes = data_bytes + 32
key_raw = secrets.token_bytes(key_bytes)
key = BitVector(rawbytes=key_raw)

cipher = data ^ key
cipher_hex = cipher.get_hex_string_from_bitvector()

with open("key.bin", "wb") as f:
    f.write(key_raw)
with open("cipher.hex", "w") as f:
    f.write(cipher_hex)
