from PIL import Image
import numpy as np
from Crypto.Cipher import AES
import os

# Cargar la imagen
image_path = "tux.bmp"
img = Image.open(image_path)
img = img.convert("RGBA")  # Asegurarse que la imagen esté en RGBA
image_array = np.array(img)

# Convertir la imagen a bytes
image_bytes = image_array.tobytes()

# Asegurarse de que el número de bytes sea múltiplo de 16
padding_length = 16 - (len(image_bytes) % 16)
padded_image_bytes = image_bytes + bytes([padding_length]) * padding_length

# Cifrar los bytes usando AES en modo ECB
key = os.urandom(16)  # Generar una clave AES de 128 bits (16 bytes)
cipher = AES.new(key, AES.MODE_ECB)
encrypted_bytes = cipher.encrypt(padded_image_bytes)

# Cortar el padding para asegurar el tamaño correcto
encrypted_bytes = encrypted_bytes[:len(image_bytes)]

# Convertir los bytes cifrados a una matriz NumPy con la forma original
encrypted_image_array = np.frombuffer(encrypted_bytes, dtype=np.uint8).reshape((405, 480, 4))

# Crear y guardar la nueva imagen
encrypted_image = Image.fromarray(encrypted_image_array, "RGBA")
encrypted_image.save("encrypted_image.png")
