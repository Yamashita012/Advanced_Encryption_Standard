# Advanced Encryption Standard (AES) Implementation in Python

This Python script demonstrates the implementation of the Advanced Encryption Standard (AES), a widely used symmetric encryption algorithm. The script allows users to encrypt and decrypt messages using AES encryption.

## Table of Contents
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Generates a banner displaying "ADVANCED ENCRYPTION STANDARD".
- Generates a security key for encryption.
- Encrypts a user-provided message using AES encryption.
- Decrypts an encrypted message using AES decryption.
- Error handling for decryption failures.

## Dependencies
- [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/src/installation.html): This script requires the `pycryptodome` library for AES encryption and decryption.

## Installation
1. Clone this repository to your local machine using:
   ```
   git clone https://github.com/yamashita012/Advanced_Encryption_Standard.git
   ```
2. Install the required dependencies using pip:
   ```
   pip install pycryptodome
   ```

## Usage
1. Run the `aes_encryption.py` script.
2. Follow the on-screen prompts:
   - Enter your message to be encrypted.
   - The script will display the encrypted message.
   - It will then decrypt the message and display the decrypted result.
