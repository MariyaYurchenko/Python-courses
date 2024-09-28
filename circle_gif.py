import sys, os
from PIL import Image
path = "making_gif"
listdir = os.listdir(path)

images = []

for img in listdir:
    image = Image.open(path + "/" + img)
    images.append(image)

images[0].save(
    "circle.gif", save_all=True, append_images=images[1:], duration = 200, loop = 0
)    