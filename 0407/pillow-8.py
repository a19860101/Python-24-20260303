from PIL import Image, ImageDraw, ImageFont
import glob

images = glob.glob('./images/*.[jJ][pP][gG]')

img = Image.open(images[0])
w,h = img.size

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('./NotoSerifTC-Black.ttf', 200)
text = '聯成電腦'
t,l,w1,h1 = draw.textbbox((0,0),text,font=font)

print(w1,h1)
# draw.text((0,0),text, font=font, fill='pink')
# draw.text((w-w1,h-h1),text, font=font, fill='pink')
# draw.text((w-w1,0),text, font=font, fill='pink')
# draw.text((0,h-h1),text, font=font, fill='pink')
# draw.text((w/2 - w1/2 , h/2-h1/2),text, font=font, fill='pink')

for y in range(0, h, int(h1)):
    for x in range(0, w, int(w1)):
        draw.text((x, y), text, font=font, fill=(255, 192, 203))

img.save('./output.jpg')

