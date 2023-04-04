from image_tools import *
import blowFish
from freq_monobit_test import *
from serial_test import *
from bitstring import BitArray
import os


#rename files in a folder
# .getcwd()
# collection = "image_data"
# for i, filename in enumerate(os.listdir(collection)):
#     os.rename("image_data/" + filename, "image_data/" + str(i) + ".jpg")

if __name__ == '__main__':
    imgs = image_list('image_data/')
    bl = blowFish.BlowFish()
    key = b'Sixteen byte key'
    # i = 0
    # for x in imgs:
    #     write_to_dir('image_encrypted_blow/'+str(i), bl.encrypt(x, key))
    #     i += 1
    true_encrypted_list = [bl.encrypt(x, key) for x in imgs]
    encrypted_list = image_list('image_encrypted_blow/')
    mono_test_data = []
    serial_test_data = []
    for x in encrypted_list:
        binary_string = bin(int.from_bytes(x, byteorder='big', signed=False))[2:]
        mono_test_data.append(freq_monobit_test(binary_string))
        serial_test_data.append(serial(binary_string))
