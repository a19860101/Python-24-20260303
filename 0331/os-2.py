import os

# 組合路徑

file_path = 'asdf/qwer/file.jpg'
new_file_path = os.path.join('asdf','qwer','file.csv')

print(new_file_path)

# 判斷路徑是否存在
is_exist = os.path.exists('test')
print(is_exist)

# 取得檔名與副檔名
filename = os.path.basename(file_path)
print(filename)

dirname = os.path.dirname(file_path)
print(dirname)

# print(os.path.splitext(filename))
name, ext = os.path.splitext(filename)
print(name)
print(ext[1:])
