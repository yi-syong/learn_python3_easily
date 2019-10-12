num_str = input('請輸入小於100000的整數:')

if 0 < int(num_str) < 100000:
    print(len(num_str),'位數')
else:
    print('輸入錯誤')