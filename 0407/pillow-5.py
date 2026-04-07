from PIL import Image
import os,glob

images = glob.glob('./images/*.[jJ][pP][gG]')

img = Image.open(images[0])
# 裁切
# box = (0,0,4000,3000)
# cropped_img = img.crop(box)
# cropped_img.save('cropped_img.jpg')

# 旋轉
# rotated_img = img.rotate(90,expand=True,fillcolor='pink')
# rotated_img.save('rotated_img.jpg')

# 翻轉
# transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# transpose_img = img.transpose(Image.FLIP_TOP_BOTTOM)
# transpose_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# transpose_img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# transpose_img = img.transpose(Image.Transpose.ROTATE_90)
# transpose_img = img.transpose(Image.Transpose.ROTATE_180)
transpose_img = img.transpose(Image.Transpose.ROTATE_270)
transpose_img.save('transpose_img.jpg')

#transpose（矩陣轉置）：
# 它是直接針對底層的像素陣列（矩陣）進行重新排列。因為它只處理完美的直角（90度的倍數）或鏡像，所以不需要做任何複雜的像素重新計算（內插法）。它的執行速度極快，且保證絕對零失真。

# rotate（幾何旋轉）：
# 它是為了「任意角度」而設計的（例如 12.5 度、45 度）。當您旋轉這類角度時，原本的像素網格無法完美對齊，Pillow 必須使用三角函數與重採樣濾波器（Resampling）來計算新位置的像素顏色。雖然現代的 Pillow 對 90/180/270 度有做優化，但它本質上仍是一個較為複雜的幾何運算函數

