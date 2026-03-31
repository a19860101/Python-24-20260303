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

    new_dir_name = rules.get(ext)

    if not os.path.exists(new_dir_name):
        os.makedirs(new_dir_name)

    new_path = os.path.join(new_dir_name,item)

    shutil.move(old_path,new_path)





