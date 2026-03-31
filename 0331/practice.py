import os
import shutil

target_dir = './00000'

new_dir = 'html'

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

all_files = os.listdir(target_dir)


for item in all_files:
    # print(os.path.basename(item))
    # print(os.path.splitext(item)[1][1:])
    name, ext = os.path.splitext(item)

    old_path = os.path.join(target_dir,item)
    new_path = os.path.join(new_dir,item)
    if ext == '.html':
        shutil.move(old_path, new_path)
