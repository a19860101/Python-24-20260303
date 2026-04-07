from PIL import Image
import os,glob

images = glob.glob('./images/*.[jJ][pP][gG]')

img = Image.open(images[0])

# box = (0,0,4000,3000)
# cropped_img = img.crop(box)
# cropped_img.save('cropped_img.jpg')

# rotated_img = img.rotate(90,expand=True,fillcolor='pink')
# rotated_img.save('rotated_img.jpg')

# transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# transpose_img = img.transpose(Image.FLIP_TOP_BOTTOM)
# transpose_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# transpose_img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# transpose_img = img.transpose(Image.Transpose.ROTATE_90)
# transpose_img = img.transpose(Image.Transpose.ROTATE_180)
transpose_img = img.transpose(Image.Transpose.ROTATE_270)
transpose_img.save('transpose_img.jpg')

