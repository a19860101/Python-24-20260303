from PIL import Image
import os,glob

images = glob.glob('./images/*.[jJ][pP][gG]')

img = Image.open(images[0])

box = (0,0,4000,3000)

cropped_img = img.crop(box)

cropped_img.save('cropped_img.jpg')