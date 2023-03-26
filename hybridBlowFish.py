# pip install pycryptodome
# pip install opencv-python
import os
from blowFish import *


def get_xor(byte_str1, byte_str2):
    byte_arr1 = bytearray(byte_str1)
    byte_arr2 = bytearray(byte_str2)
    # Perform the bitwise XOR operation on the bytearrays
    result_arr = bytearray([a ^ b for a, b in zip(byte_arr1, byte_arr2)])
    # Convert the result bytearray back to a byte string
    return bytes(result_arr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_path = get_image_path()
    image_byte = get_image_bytes(image_path)

    key = b'Sixteen byte key'
    byte_size = os.path.getsize(image_path)
    randValue = np.random.bytes(byte_size)
    message = get_xor(image_byte, randValue)

    display_image(message, 'This is the randomized image')
    # Generate a new initialization vector (IV)
    iv = get_random_bytes(Blowfish.block_size)

    # Create a Blowfish cipher object and encrypt the message
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message, Blowfish.block_size))
    # display the encrypted image if its corrupted print random one
    print(ciphertext)
    display_image(ciphertext, 'This is the encrypted randomized image')

    # Now decrypt the image and print the decrypted one
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
    # display the decrypted image before removing the random value
    display_image(plaintext, 'This is the decrypted randomized image')
    # display the image after removing the random value
    plaintext = get_xor(plaintext, randValue)
    display_image(plaintext, 'The decrypted image after removing the random value')
    print(plaintext)
