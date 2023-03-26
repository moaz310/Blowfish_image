# pip install pycryptodome
# pip install opencv-python

import random
import cv2
import numpy as np
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def get_image_path():
    import tkinter as tk
    from tkinter import filedialog
    # Create a root window
    root = tk.Tk()
    root.withdraw()
    # Create a file dialog box and get the selected file path
    file_path = filedialog.askopenfilename()
    # Print the selected file path
    print("Selected file path:", file_path)
    return file_path


def get_image_bytes(path):
    with open(path, 'rb') as f:
        byte_im = f.read()
        return byte_im


def display_image(image_bytes, name):
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    if image is None:
        # Create a random image
        height, width = 480, 640
        image = np.zeros((height, width, 3), dtype=np.uint8)
        image[:, :, :] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        # Display the random image
        cv2.imshow(name, image)
    else:
        # Display the decoded image
        cv2.imshow(name, image)
    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_path = get_image_path()
    image_byte = get_image_bytes(image_path)

    key = b'Sixteen byte key'
    message = image_byte

    # Generate a new initialization vector (IV)
    iv = get_random_bytes(Blowfish.block_size)

    # Create a Blowfish cipher object and encrypt the message
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message, Blowfish.block_size))
    # display the encrypted image if its corrupted print random one
    print(ciphertext)
    display_image(ciphertext, 'This is the encrypted image')

    # Now decrypt the image and print the decrypted one
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
    # display the decrypted image
    display_image(plaintext, 'This is the decrypted image')
    print(plaintext)
