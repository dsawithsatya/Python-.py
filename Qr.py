import qrcode
url=input("Enter the url here")
img=qrcode.make(url)
img.save("Github.png")
print("QR created successfully")