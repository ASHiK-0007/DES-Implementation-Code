# DES Encryption and Decryption using Python

## Overview

This project demonstrates the implementation of the Data Encryption Standard (DES) algorithm using Python and the PyCryptodome library.

The application allows users to encrypt plaintext messages and decrypt ciphertext using a DES key. DES is a symmetric-key block cipher that operates on 64-bit data blocks using a 56-bit effective key.

## Features

* DES Encryption
* DES Decryption
* ECB (Electronic Codebook) Mode
* Automatic Padding and Unpadding
* Hexadecimal Ciphertext Output
* Simple and Easy-to-Understand Python Implementation

## Project Structure

```text
DES-Implementation/
│
├── des.py
├── test.py
└── README.md
```

## Requirements

* Python 3.x
* PyCryptodome

Install the required package:

```bash
pip install pycryptodome
```

## How It Works

1. A DES key of exactly 8 bytes is provided.
2. The plaintext is padded to match the DES block size.
3. The plaintext is encrypted using DES in ECB mode.
4. The encrypted output is displayed in hexadecimal format.
5. The ciphertext can be decrypted back to the original plaintext using the same key.

## Running the Program

Run the main file:

```bash
python des.py
```

Run the test file:

```bash
python test.py
```

## Example Output

```text
Encrypted: 6f2c...
Decrypted: Hello DES

Original : Cyber Security Lab
Encrypted: 8a7f...
Decrypted: Cyber Security Lab
```

## Files Description

### des.py

Contains the DESAlgorithm class with:

* Key validation
* Encryption function
* Decryption function

### test.py

Contains example usage and testing of the DES implementation.

## Learning Objectives

* Understand symmetric key cryptography
* Learn the basics of DES encryption and decryption
* Work with Python cryptographic libraries
* Implement secure data transformation using encryption algorithms

## Author

Ashik Islam
