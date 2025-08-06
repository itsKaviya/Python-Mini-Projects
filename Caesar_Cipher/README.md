# 🔐 Caesar Cipher Program (Python)

This Python script implements the **Caesar Cipher**, a classic encryption technique where each letter in the plaintext is shifted by a fixed number of positions down the alphabet. This version supports **both encoding and decoding**, as well as punctuation and whitespace handling.

## 🧩 Features

* Supports **encoding** (encrypting) and **decoding** (decrypting)
* Handles lowercase letters, spaces, and punctuation
* Wraps shifts greater than 26 using modulo logic
* Looping interface: users can run the cipher multiple times
* ASCII logo display on startup (optional)

## 📜 Code Highlights

* **Alphabet Wrapping**: The alphabet list is repeated to handle wrap-around logic without index errors.
* **Shift Normalization**: Any shift > 26 is normalized with `shift = shift % 26`.
* **Robust Logic**: Characters not in the alphabet (e.g., spaces, punctuation) are not altered.
* **Looping Interface**: Lets user run the cipher repeatedly until they choose to exit.

## 📌 Notes

* Only lowercase letters are supported for transformation. Inputs are automatically converted to lowercase.
* You can expand this project to support:

  * Uppercase letters
  * GUI or web interface
  * File encryption/decryption