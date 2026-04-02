from PIL import Image

img = Image.open('./images/shana-van-roosbroek-gdPqNWGfqW4-unsplash.jpg')

print(img)
print(img.size)
print(img.mode)
print(img.format)

img.show()

img.save('test.jpg')