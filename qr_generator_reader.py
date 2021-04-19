import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
from tkinter.filedialog import *

while True:
    choice = int(input("Enter 1 to generate QR code and 2 to read QR code: "))
    if choice == 1:
        text = input("Enter the text you want to convert into QR code: ")

        qr = pyqrcode.create(text)
        qr.png("myCode.png", scale=8)

    elif choice == 2:
        # img = input("Enter the name of the image that contains the QR code, please enter the correct name in case sensitive: ")
        img = askopenfilename()

        d = decode(Image.open(f"{img}"))
        print(d[0].data.decode("ascii"))

    else:
        print("You entered something else.\nTry Again... ")

    loop_out = input("Enter q to quit this loop: ")

    if loop_out == 'q':
        break