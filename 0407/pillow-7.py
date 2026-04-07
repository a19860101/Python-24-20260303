from PIL import Image, ImageDraw
import glob

images = glob.glob('./images/*.[jJ][pP][gG]')

img = Image.open(images[0])

w,h = img.size

draw = ImageDraw.Draw(img)

draw.text((w-1200,h-200),"聯電", font_size=200)

img.show()