# pip install pycryptodome
# pip install opencv-python

from image_tools import *
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

class BlowFish:
    def __init__(self):
        with open('iv.txt', 'rb') as fd:
            self.iv = fd.readline()

    def encrypt(self, message, key):
        # Create a Blowfish cipher object and encrypt the message
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, self.iv)
        return cipher.encrypt(pad(message, Blowfish.block_size))

    def decrypt(self, ciphertext, key):
        # Now decrypt the image and print the decrypted one
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(ciphertext), Blowfish.block_size)


if __name__ == '__main__':
    image_path = get_image_path()
    image_byte = get_image_bytes(image_path)
    key = b'Sixteen byte key'
    message = image_byte
    bl1 = BlowFish()
    ciphertext = bl1.encrypt(message=message, key=key)
    # display the encrypted image if its corrupted print random one
    print(ciphertext)
    display_image(ciphertext, 'This is the encrypted image')

    # Now decrypt the image and print the decrypted one
    plaintext = bl1.decrypt(ciphertext=ciphertext, key=key)

    # display the decrypted image
    display_image(plaintext, 'This is the decrypted image')
    print(plaintext)
