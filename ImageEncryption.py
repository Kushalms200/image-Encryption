from PIL import Image
from cryptography.fernet import Fernet
import io

# Read the image path from user input
image_path = input("Enter the path to your image file: ")

# Load the image
image = Image.open(image_path)

# Convert the image to bytes
image_bytes = io.BytesIO()
image.save(image_bytes, format='JPEG')
image_bytes = image_bytes.getvalue()

# Generate a strong key for encryption (AES-256)
key = Fernet.generate_key()

# Encrypt the image bytes
cipher = Fernet(key)
encrypted_image_bytes = cipher.encrypt(image_bytes)

# Save the encrypted image bytes to a new file
encrypted_image_path = 'encrypted_image.jpg'
with open(encrypted_image_path, 'wb') as f:
    f.write(encrypted_image_bytes)

print(f"Image encrypted and saved as '{encrypted_image_path}'")
print(f"Encryption key: {key.decode()}")
