# Chapter 15

### 15.1
> 1
### 15.2
> 2
### 15.3
> 4
### 15.4
```python=
num_list = []
for i in range(1,11):
    print('請輸入第', i, '個數字')
    num = int(input(':'))
    num_list += [num]

print(num_list)
print('最大值:', max(num_list), '最小值:', min(num_list))
```
### 15.5
> 1 & 2

因為 for 迴圈沒有 ':'
第三行應為 '+='

### 15.6
>4
### 15.7
```python=
num1, num2 = input('請輸入兩個介於0和100之間的數字:').split()
num1 = float(num1)
num2 = float(num2)

if num1 < 0 or num1 > 100 or num2 < 0 or num2 > 100 :
    print('數字範圍不符合條件')
else:
    average = (num1 + num2) / 2;
    print("兩個數的平均:", average)
```
### 15.8
>4

### 15.9
請自行完成