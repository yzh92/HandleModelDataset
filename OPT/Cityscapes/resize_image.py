from PIL import Image
import os

root_path = ''
image_names = os.listdir(root_path)

for name in image_names:
    im = Image.open(name)
    resize_image = im.resize((512,1024))
    resize_image.save(f'./resize_data/{name}','png')
