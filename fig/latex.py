from PIL import Image

for ite in range(iterations):
    img = Image.open('roc/roc_'+str(ite)+".png")
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for it in datas:
        if it[0] == 255 and it[1] == 255 and it[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(it)
    img.putdata(newData)
    img.save('roc/roc_'+str(ite)+".png", "PNG")

for ite in range(iterations):
    back = Image.open("roc/roc_1.png")
    fore = Image.open("roc/roc_"+str(ite)+".png")
    Image.alpha_composite(back, fore).save("roc/roc_1.png")