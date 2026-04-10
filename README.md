# bitvector-xor-cipher

Implementation of XOR cipher with Zero Padding using BitVector library.
Educational project demonstrating symmetric encryption, one-time pad principles, and block alignment techniques.

**For educational purposes only**

## Overview

This project implements a simple XOR-based symmetric cipher. It reads arbitrary input (text or file), applies zero padding to align data to 128-bit blocks, and encrypts it using a cryptographically secure random key generated with Python's `secrets` module.

## How It Works

| Step | Description |
|------|-------------|
| Input | Text string or binary file |
| Padding | Zero padding applied to reach 128-bit block alignment |
| Key Generation | Random key longer than plaintext by 32 bytes (256 bits) |
| Encryption | Bitwise XOR operation (`cipher = data ^ key`) |
| Output | Key saved as `.bin`, ciphertext saved as `.hex` |

## Features

- XOR cipher following one-time pad principles
- Zero padding for block alignment
- Cryptographically secure key generation via `secrets`
- Bit-level operations using BitVector library
- Supports both plaintext strings and binary files

## Files

| File | Description |
|------|-------------|
| `xor_encrypt.py` | Encryption script |
| `xor_decrypt.py` | Decryption script |

## Requirements

- Python 3.6+
- BitVector library

## Installation

```bash
pip install BitVector
```

## Security Analysis (Educational)

This implementation demonstrates the mathematical strength of the One-Time Pad: with a truly random key the same length as the message or longer, the ciphertext is unbreakable by cryptanalysis.

However, the following real-world limitations exist:

| # | Limitation | Explanation |
|---|---|---|
| 1 | No integrity protection | The ciphertext can be modified without detection. An attacker who knows or guesses part of the plaintext can perform a bit-flipping attack to alter the decrypted message. |
| 2 | Key management problem | The key must be the same length as the message or longer and securely transmitted to the recipient. In practice, this makes OTP impractical for most use cases. |
| 3 | No authentication | The recipient cannot verify who sent the message or whether it was tampered with. |
| 4 | Single-use only | Reusing the same key for two different messages breaks the security completely (two-time pad attack). |

> This project is intended to teach cryptographic primitives, not to be deployed in production.

## Disclaimer

This cipher is intended for educational demonstration only. It is not suitable for production use. For real-world applications, use established authenticated encryption algorithms such as:

- **AES-256-GCM**
- **ChaCha20-Poly1305**
