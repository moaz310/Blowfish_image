# pip install pycryptodome
# pip install opencv-python
import os
from blowFish import BlowFish
from image_tools import *


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

    bl = BlowFish()
    display_image(message, 'This is the randomized image')

    # Create a Blowfish cipher object and encrypt the message
    ciphertext = bl.encrypt(message=message, key=key)
    # display the encrypted image if its corrupted print random one
    display_image(ciphertext, 'This is the encrypted randomized image')
    print(ciphertext)

    # Now decrypt the image and print the decrypted one
    plaintext = bl.decrypt(ciphertext=ciphertext, key=key)
    # display the decrypted image before removing the random value
    display_image(plaintext, 'This is the decrypted randomized image')
    # display the image after removing the random value
    plaintext = get_xor(plaintext, randValue)
    display_image(plaintext, 'The decrypted image after removing the random value')
    print(plaintext)
