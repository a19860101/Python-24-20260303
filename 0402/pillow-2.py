from PIL import Image
import os

img = Image.open('./images/shana-van-roosbroek-gdPqNWGfqW4-unsplash.jpg')

os.makedirs('./thumbs', exist_ok=True)

img.save('thumbs/test.jpg', quality=75)