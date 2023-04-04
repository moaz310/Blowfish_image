# pip install pycryptodome
# pip install opencv-python
import os
from blowFish import BlowFish
from image_tools import *


class HybridBlowFish:
    def __init__(self):
        self.bl = BlowFish()

    @staticmethod
    def get_xor(byte_str1, byte_str2):
        byte_arr1 = bytearray(byte_str1)
        byte_arr2 = bytearray(byte_str2)
        # Perform the bitwise XOR operation on the bytearrays
        result_arr = bytearray([a ^ b for a, b in zip(byte_arr1, byte_arr2)])
        # Convert the result bytearray back to a byte string
        return bytes(result_arr)

    def encrypt(self, message, key, randValue):
        message = self.get_xor(message, randValue)
        display_image(message, 'This is the randomized image')
        return self.bl.encrypt(message=message, key=key)

    def decrypt(self, cipher, key, randValue):
        # Now decrypt the image and print the decrypted one
        plaintext = self.bl.decrypt(ciphertext=cipher, key=key)
        # display the decrypted image before removing the random value
        display_image(plaintext, 'This is the decrypted randomized image')
        return self.get_xor(plaintext, randValue)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_path = get_image_path()
    image_byte = get_image_bytes(image_path)
    key1 = b'Sixteen byte key'
    byte_size = os.path.getsize(image_path)
    randomValue = np.random.bytes(byte_size)

    # Create a hybridBlowfish cipher object and encrypt the message
    hybrid_bl = HybridBlowFish()
    ciphertext = hybrid_bl.encrypt(message=image_byte, key=key1, randValue=randomValue)
    # display the encrypted image if its corrupted print random one
    display_image(ciphertext, 'This is the encrypted randomized image')
    print(ciphertext)

    # display the image after removing the random value
    plain = hybrid_bl.decrypt(cipher=ciphertext, key=key1, randValue=randomValue)
    display_image(plain, 'The decrypted image after removing the random value')
    print(plain)
