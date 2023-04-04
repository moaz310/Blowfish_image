import random
import cv2
import numpy as np


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

def write_to_dir(dir, image):
    with open(dir + '.jpg', 'wb') as f:
        f.write(image)

def imge_list(path):
    imgs = [get_image_bytes(path+str(x)+'.jpg') for x in range(0, 100)]
    return imgs