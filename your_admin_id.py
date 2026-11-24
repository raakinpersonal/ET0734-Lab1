file=open("devices","r")
for item in file:
    item=item.strip()
    print(item)
file.close()
