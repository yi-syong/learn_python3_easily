# Chapter 20

### 20.1
>2

### 20.2
```
except
```

### 20.3
```python=
import random

students = {}
id = 1

for c in range(65, 91):
    name = chr(c) + chr(c) + chr(c)
    
    score1 = random.randint(0, 100)
    score2 = random.randint(0, 100)
    score3 = random.randint(0, 100)
    
    if id < 10:
        id_string = 'T00' + str(id)
    else:
        id_string = 'T0' + str(id)
        
    students[id_string] = (name, score1, score2, score3)
    
    id += 1
    if id > 20:
        break;

input_id = input('請輸入學號(T001 ~ T020) :')

try:
    print(students[input_id])
    
    modify = input('是否要修改學生資料(是請輸入Y或y):')
    if modify == 'Y' or modify == 'y':
        new_name = input('學生姓名:')
        new_score1 = input('第一科成績:')
        new_score2 = input('第二科成績:')
        new_score3 = input('第三科成績:')
        students[input_id] = (new_name, new_score1, new_score2, new_score3)
        print('修改後的學生資料：', students[input_id])
        
except KeyError:
    print('找不到此學號')
```
### 20.4
>4

### 20.5
>1

### 20.6
```python=
x = 5
try:
    len(x)
except TypeError:
    print('無法操作')
```
```python=
x = [1, 2, 3]
y = {1, 2, 4}

try:
    z = x & y
except TypeError:
    print('無法操作')
```

