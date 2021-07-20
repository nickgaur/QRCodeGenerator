import qrcode


qr = (input("Enter A URL or qr code data: "))

img = qrcode.make(qr)
img.save('qr_code.png')
img.show()
