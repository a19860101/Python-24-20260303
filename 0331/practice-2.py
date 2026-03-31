import os
import shutil

target_dir = './00000'

rules = {
    '.html':'網頁檔',
    '.txt':'文字檔',
    '.jpg': '圖片檔',
    '.py': '大蟒蛇'
}
all_files = os.listdir(target_dir)

# print(rules['.html'])
print(rules.get('.html'))
for item in all_files:
    old_path = os.path.join(target_dir,item)
    name,ext = os.path.splitext(item)
    ext = ext.lower()

    if not os.path.exists(rules.get(ext)):
        os.makedirs(rules.get(ext))





