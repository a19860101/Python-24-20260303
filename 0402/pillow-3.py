from PIL import Image
import os,glob

images = glob.glob('./images/*.jpg')
print(images)
img = Image.open(images[0])
# img = Image.open('./images/shana-van-roosbroek-gdPqNWGfqW4-unsplash.jpg')

w1, h1 = img.size

w2 = int(input('請輸入縮圖的寬：'))

h2 = int((h1 * w2) / w1)

small_img = img.resize((w2,h2))

os.makedirs('./thumbs', exist_ok=True)

small_img.save('thumbs/test.jpg', quality=75)