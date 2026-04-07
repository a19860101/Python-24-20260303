from PIL import Image, ImageDraw, ImageFont
import glob

images = glob.glob('./images/*.[jJ][pP][gG]')

img = Image.open(images[0])

w,h = img.size

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('./NotoSerifTC-Black.ttf', 200)

# draw.text((w-1200,h-200),"聯電", font_size=200,font=font)
draw.text((0,0),"聯成電腦",font=font, fill="red")

# img.show()
img.save('./output.jpg')