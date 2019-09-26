# Chapter 19

### 19.1
>4

### 19.2
```
for
```
### 19.3
> 3 

是 remove

### 19.4
>4

### 19.5
>4

### 19.6
>1

### 19.7
>2

### 19.8
```python=
import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = set(random.sample(letters, 10))
t = set(random.sample(letters, 10))
u = set(random.sample(letters, 10))

print('沒有被挑到的字母:', set(letters)-(s | t | u))
print('被挑到一次的字母:', (s ^ t ^ u)-(s & t & u))
print('被挑到兩次的字母:', ((s & t)|(t & u)|(s & u))-(s & t & u))
print('被挑到三次的字母:', s & t & u)
```

### 19.9
>3

### 19.10
>2

### 19.11
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
print(students[input_id])

modify = input('是否要修改學生資料(是請輸入Y或y):')

if modify == 'Y' or modify == 'y':
    new_name = input('學生姓名:')
    new_score1 = input('第一科成績:')
    new_score2 = input('第二科成績:')
    new_score3 = input('第三科成績:')
    students[input_id] = (new_name, new_score1, new_score2, new_score3)
    print('修改後的學生資料：', students[input_id])
```