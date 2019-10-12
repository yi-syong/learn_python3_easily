num1 = int(input('請輸入第一個正整數:'))
num2 = int(input('請輸入第二個正整數:'))
common_factor=[]

if num1 > num2:
    num1, num2 = num2, num1

for i in range(1, num1+1, 1):
    if num1 % i == 0 and num2 % i == 0:
        common_factor += [i]

print(num1, '與', num2,'的所有公因數', common_factor)