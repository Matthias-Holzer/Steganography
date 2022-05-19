from PIL import Image
import numpy as np

def encode():
    img = Image.open("img.png")
    arr = np.array(img, dtype=np.uint8)
    bina = np.unpackbits(arr[..., None], axis=-1)
    mes = "9"
    bmes = bytearray(mes, "utf8")
    blist = ""
    for b in bmes:
        blist += bin(b)[2:]
    print(blist)
    c = 0
    for il, line in enumerate(bina):
        for ip, pixel in enumerate(line):
            for iv, value in enumerate(pixel):
                if c < len(blist):
                    bina[il][ip][iv][6] = blist[c]
                    c += 1
                    bina[il][ip][iv][7] = blist[c]
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
                #print(bina[il][ip][iv])
                l += str(bina[il][ip][iv][6])
                l += str(bina[il][ip][iv][7])
    print(l)
    img2 = Image.open("img.png")
    arr2 = np.array(img2, dtype=np.uint8)
    print(f"in: {arr2}")
    print(f"out: {arr}")
    #print(f"equal: {arr==arr2}")
    exit()
    # convert above string to int with base 2
    binary_int = int(l, 2)
    # get the byte number
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()

    print(ascii_text)  # python
    Image.fromarray(arr).save("out.jpg")

encode()
decode()
