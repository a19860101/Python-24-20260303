

class TestError(Exception):
    pass


try:
    age = input('請輸入年齡：')
    if not age.isdigit():
        raise ValueError('請輸入數字')
    else:
        age = int(age)
    if age < 0:
        raise TestError('年齡不可為負數')

    if age < 18:
        raise ValueError('未滿18禁止進入！')
except ValueError as e:
    print(e)
except TestError as e:
    print(e)


finally:
    print('------程式結束!!------')


