import binascii
from PIL import Image
import numpy as np


def encode():
    img = Image.open("img.jpg")
    arr = np.array(img, dtype=np.uint8)
    bina = np.unpackbits(arr[..., None], axis=-1)
    file = open("message.txt", "r")
    mes = file.read()
    bmes = "".join(f"{ord(i):08b}" for i in mes)
    bmes += "00011010"  # End Of File ascii
    c = 0
    for il, line in enumerate(bina):
        for ip, pixel in enumerate(line):
            for iv, value in enumerate(pixel):
                if c < len(bmes):
                    bina[il][ip][iv][6] = bmes[c]
                    c += 1
                if c < len(bmes):
                    bina[il][ip][iv][7] = bmes[c]
                    c += 1
    y = np.packbits(bina, axis=-1)
    z = np.squeeze(y, axis=-1)
    Image.fromarray(z).save("out.png")


def decode():
    img = Image.open("out.png")
    arr = np.array(img, dtype=np.uint8)
    bina = np.unpackbits(arr[..., None], axis=-1)
    l = ""
    for il, line in enumerate(bina):
        for ip, pixel in enumerate(line):
            for iv, value in enumerate(pixel):
                l += str(bina[il][ip][iv][6])
                l += str(bina[il][ip][iv][7])

    ll = [l[i:i + 8] for i in range(0, len(l), 8)]
    mes = ""
    for b in ll:
        dec = int(b, 2)
        if dec == 26:
            break
        mes += chr(dec)

    print("The hidden message inside the given image is: ")
    print(mes)


encode()
decode()
