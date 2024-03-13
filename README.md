# Image Encryption

This Python script allows you to encrypt image files using strong encryption (AES-256) provided by the cryptography library. The encrypted images can be securely stored or transmitted over the internet, ensuring that only authorized parties with the correct key can decrypt and access the original image.

# Features

Strong Encryption: Utilizes AES-256 encryption for strong and secure encryption of image files.

Simple Usage: Easy-to-use script that prompts the user for the image file path and generates a unique encryption key.

Secure Key Management: The encryption key is generated securely and is required for decryption, ensuring the security of encrypted images.

# How to Use

Clone the repository or download the encrypt_image.py script.

Install the required libraries using pip install Pillow cryptography.

Run the script and provide the path to the image file you want to encrypt.

The script will generate a unique encryption key and save the encrypted image as encrypted_image.jpg.

Note: Keep the encryption key secure and do not share it with unauthorized parties. Without the key, the encrypted image cannot be decrypted.
