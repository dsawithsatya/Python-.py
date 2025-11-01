f=open("satya.txt","w")
text=f.write("Peoples are good")
with open("satya.txt","r+") as f:
    text=f.read()
    f.seek(12)
    print(f.tell())
    text=f.write("Very Bad")
    