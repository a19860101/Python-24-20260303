while True:
    mode = input('請選擇功能：美金轉台幣輸入1，台幣轉美金輸入2，或輸入q結束程式：')
    if mode == 'q':
        print('掰!!')
        break
    rate = 32.1
    if mode == '1':
        m = float(input('請輸入美金：'))
        result = m * rate
        print(f'美金{m:,}約等於台幣{result:,.2f}')

    elif mode == '2':
        m = float(input('請輸入台幣：'))
        result = m / rate
        print(f'台幣{m:,}約等於美金{result:,.2f}')

    else:
        print('輸入錯誤')