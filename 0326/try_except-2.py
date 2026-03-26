try:
    age = int(input('請輸入年齡：'))
    if age < 0:
        raise ValueError('年齡不可為負數')

    if age < 18:
        raise ValueError('未滿18禁止進入！')
except ValueError as e:
    print(e)

finally:
    print('------程式結束!!------')

