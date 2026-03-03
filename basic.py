# 變數

## 變數命名規範

'''
1. 只可使用英文、數字與底線
2. 不可使用數字開頭
3. 大小寫有別
4. 不可使用關鍵字
'''

# 查詢關鍵字
import keyword
print(keyword.kwlist)

## 資料型別

# 整數 int integer
a = -15
# print(a)
print(type(a))

# 浮點數 float
b = 1.000
print(type(b))

# 複數 complex
cx = 2j
print(type(cx))

# 字串 str string
# c = 'hello'
# c = "hello"
c = '123'
print(type(c))


# 布林 bool boolean
t = True
f = False
print(type(t))
print(type(f))

# 命名風格
# snake
# student_name = ''
# camel
# studentName = ''
# pascal
# StudentName = ''