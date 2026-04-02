from PIL import Image
import os,glob

images = glob.glob('./images/*.[jJ][pP][gG]')
print(images)

for image in images:
    img_name = os.path.basename(image)
    img = Image.open(image)
    w1, h1 = img.size
    w2 = 200
    h2 = int((h1 * w2) / w1)
    s_img = img.resize((w2,h2))
    os.makedirs('./thumbs', exist_ok=True)
    s_img.save(f'./thumbs/s_{img_name}', quality=1)

# for i,image in enumerate(images):
#     name,ext = os.path.splitext(image)
#     img = Image.open(image)
#     w1, h1 = img.size
#     w2 = 200
#     h2 = int((h1 * w2) / w1)
#     s_img = img.resize((w2,h2))
#     os.makedirs('./thumbs', exist_ok=True)
#     s_img.save(f'./thumbs/{i+1}{ext}', quality=1)

