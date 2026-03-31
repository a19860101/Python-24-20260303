import os

# 取得目前工作目錄
current_dir = os.getcwd()
print(current_dir)
# os.mkdir('test')

# 切換工作目錄
# os.chdir('../0326')
# print(os.getcwd())
# os.mkdir('test2')

# 列出
# print(os.listdir())

# 建立資料夾
# os.mkdir('test/123')
# os.makedirs('qwer/asdf/zxcv')

# 刪除資料夾
# os.rmdir('test')

# 刪除檔案
os.remove('test/asdf.py')
