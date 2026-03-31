import os

target_dir = '00000'

all_files = os.listdir(target_dir)

for item in all_files:
    # print(os.path.basename(item))
    # print(os.path.splitext(item)[1][1:])
    name, ext = os.path.splitext(item)
    print(ext)