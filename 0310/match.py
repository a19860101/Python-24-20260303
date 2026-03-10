# match

day = 123123123

# if day == 0:
#     print('星期日')
# elif day == 1:
#     print('星期一')

# 3.10
match day:
    case 0:
        print('星期日')
    case 1:
        print('星期一')
    case 2:
        print('星期二')
    case 3:
        print('星期三')
    case 4:
        print('星期四')
    case 5:
        print('星期五')
    case 6:
        print('星期六')
    case _:
        print('系統錯誤')

match day:
    case 1|2|3|4|5 :
        print('營業中')
    case 0|6 :
        print('放假')
    case _:
        print('系統錯誤')