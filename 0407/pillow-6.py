from PIL import Image, ImageEnhance
import glob

images = glob.glob('./images/*.[jJ][pP][gG]')

img = Image.open(images[0])

# 對比
# contrast = ImageEnhance.Contrast(img)
# img = contrast.enhance(0.1)

# 亮度
# brightness = ImageEnhance.Brightness(img)
# img = brightness.enhance(0.3)

# 飽和度
# color = ImageEnhance.Color(img)
# img = color.enhance(0)

# 銳利度
sharpness = ImageEnhance.Sharpness(img)
img1 = sharpness.enhance(0.1)
img2 = sharpness.enhance(5)
img1.save('img1.jpg')
img2.save('img2.jpg')

# img_1 = ImageEnhance.Contrast(img).enhance(0.2)
# img_2 = ImageEnhance.Brightness(img_1).enhance(3)
# img_3 = ImageEnhance.Color(img_2).enhance(0)

# img_3.show()


