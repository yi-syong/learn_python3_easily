# Chapter 10

### 10.1
```
第一個空格: in 
第二個空格: range
```
### 10.2
```
第一個空格: or
第二個空格: break
```
### 10.3
```python=
sum = 0
for i in range(1, 101, 2):
    sum += i
```

### 10.4
```python=
#第一種
sum = 0
for i in range(1, 1001, 1):
    if i % 43 == 0:
        sum += i
```
```python=
#第二種
sum = 0
for i in range(43, 1001, 43):
    sum += i
```
當然，第二種方法快非常多
### 10.5
```python=
num1 = int(input('請輸入第一個正整數:'))
num2 = int(input('請輸入第二個正整數:'))
common_factor=[]

if num1 > num2:
    num1, num2 = num2, num1

for i in range(1, num1+1, 1):
    if num1 % i == 0 and num2 % i == 0:
        common_factor += [i]

print(num1, '與', num2,'的所有公因數', common_factor)
```

### 10.6
```python=
import random as rand

for i in range(0, 3, 1):
    rand_num1 = rand.randint(0,1)
    rand_num2 = rand.randint(0,1)
    
    if rand_num1 + rand_num2 == 1:
        print("聖筊")
    else:
        print("失敗")
        break

else:
    print("連續三個聖筊")
```

### 10.7
```python=
for i in range(3, 8):
    for j in range(3, 8):
        print(i, 'x', j, '=', i*j)
    print('----------')
```

### 10.8
```python=
for i in range(1, 11):
    print(i, end=':')
    for j in range(1, i+i):
        if i % j == 0:
            print(j, end=',')
    print()
```

