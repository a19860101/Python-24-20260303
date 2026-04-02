from PIL import Image
import os,glob

images = glob.glob('./images/*.[jJ][pP][gG]')
print(images)

for image in images:
    img_name = os.path.basename(image)
    img = Image.open(image)
    os.makedirs('./thumbs', exist_ok=True)
    img.save(f'./thumbs/s_{img_name}', quality=1)

for i,image in enumerate(images):
    name,ext = os.path.splitext(image)
    img = Image.open(image)
    os.makedirs('./thumbs', exist_ok=True)
    img.save(f'./thumbs/{i+1}{ext}', quality=1)

# # img = Image.open('./images/shana-van-roosbroek-gdPqNWGfqW4-unsplash.jpg')
#
# w1, h1 = img.size
#
# w2 = int(input('請輸入縮圖的寬：'))
#
# h2 = int((h1 * w2) / w1)
#
# small_img = img.resize((w2,h2))
#

#
# small_img.save('thumbs/test.jpg', quality=75)