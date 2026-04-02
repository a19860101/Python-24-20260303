import os
import shutil
import sys

target_dir = './'

rules = {
    '.html':'網頁檔',
    '.txt':'文字檔',
    '.jpg': '圖片檔',
    '.py': '大蟒蛇'
}
all_files = os.listdir(target_dir)

self_file = os.path.basename(sys.argv[0])

print(self_file)

# print(rules['.html'])
print(rules.get('.html'))
for item in all_files:
    old_path = os.path.join(target_dir,item)
    name,ext = os.path.splitext(item)
    ext = ext.lower()

    if self_file == item:
        continue

    new_dir_name = rules.get(ext,'其他')

    if not os.path.exists(new_dir_name):
        os.makedirs(new_dir_name)

    new_path = os.path.join(new_dir_name,item)

    print(new_path)

    # shutil.copyfile(old_path,new_path)
    shutil.move(old_path,new_path)

input('按兩下enter退出...')





