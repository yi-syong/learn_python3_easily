# Chapter 11

### 11.1
>2

### 11.2
```
第一個空格: scores

第二個空格: item
```

### 11.3
```python=
my_friend1 = 'John', '男', 18, '0912333333'
my_friend2 = 'Carol', '女', 17, '0912666666'
my_friend3 = 'Lisa', '女', 16, '0912999999'
```

### 11.4
```python=
contact = my_friend1, my_friend2, my_friend3
```

### 11.5
```python=
for item in contact:
    print(item)
```

### 11.6
>4

count()方法只能用在Tuple

### 11.7
```
[item]
```

### 11.8
```python=
my_friend1 = ['John', '男', 18] 
my_friend2 = ['Carol', '女', 17]
my_friend3 = ['Lisa', '女', 16]
```

### 11.9
```python=
my_friend1.append('0912333333')
my_friend2.append('0912666666')
my_friend3.append('0912999999')
```

### 11.10
```python=
contact = [ my_friend1, my_friend2, my_friend3]
```

### 11.11
```python=
contact.append(['Tom', '男', 20, '0912555555'])
```

### 11.12
```python=
for item in contact:
    print(item)
```

### 11.13
```python=
num_student = int(input("請輸入學生人數:"))

score_list = []
for i in range(0, num_student):
    score = int(input("請輸入學生成績:"))
    score_list += [score]

pass_count = 0
fail_count = 0
for item in score_list:
    if item >= 60:
        pass_count += 1
    if item < 60:
        fail_count += 1

print("及格學生人數:", pass_count)
print("不及格學生人數:", fail_count)
```