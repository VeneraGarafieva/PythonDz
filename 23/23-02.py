from PIL import Image

im = Image.open("Рианна.jpeg")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения

for i in range(x):
    for j in range(y):
        pass
        r, g, b = pixels[i, j]


im.save("Рианна2.jpg")

