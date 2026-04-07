from PIL import Image, ImageDraw, ImageFont
import glob

images = glob.glob('./images/*.[jJ][pP][gG]')

img = Image.open(images[0])
w,h = img.size

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('./NotoSerifTC-Black.ttf', 200)

t,l,w1,h1 = draw.textbbox((0,0),'我',font=font)

print(w1,h1)
