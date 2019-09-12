# Chapter 16

### 16.1
由高到低
```python=
sorted_scores = []
scores = [60, 10, 90, 100, 20, 30, 80, 50, 40, 70]
for i in range(0, len(scores)):
    max_score = 0
    max_score_index = 0
    for j, data in enumerate(scores):
        if data > max_score:
            max_score = data
            max_score_index = j
            
    highest_score = scores.pop(max_score_index)
    sorted_scores += [highest_score]
```
由低到高
```python=
sorted_scores = []
scores = [60, 10, 90, 100, 20, 30, 80, 50, 40, 70]
for i in range(0, len(scores)):
    min_score = max(scores)
    min_score_index = 0
    for j, data in enumerate(scores):
        if data < min_score:
            min_score = data
            min_score_index = j
            
    lowest_score = scores.pop(min_score_index)
    sorted_scores += [lowest_score]
```
### 16.2
>4

### 16.3
第一個空格: 1
第二個空格: 6

### 16.4
>3
### 16.5
```python=
import random

student_score = []

for i in range(0,100):
    random_score = random.randint(0,100)
    student_score += [random_score]
    
print(student_score)
```
### 16.6
```python=
import random

dice_num = []

for i in range(0,100):
    random_num = random.randint(1,6)
    dice_num += [random_num]
    
print(dice_num)
```
### 16.7
```python=
import random

dice_num = []
for i in range(0,100):
    random_num = random.randint(1,6)
    dice_num += [random_num]

count = [0 for i in range(0,6)]
for j, point in enumerate(dice_num):
    if point == 1:
        count[0]+=1
    if point == 2:
        count[1]+=1
    if point == 3:
        count[2]+=1
    if point == 4:
        count[3]+=1
    if point == 5:
        count[4]+=1
    if point == 6:
        count[5]+=1

print("1點 -", count[0], "次")
print("2點 -", count[1], "次")
print("3點 -", count[2], "次")
print("4點 -", count[3], "次")
print("5點 -", count[4], "次")
print("6點 -", count[5], "次")
print("總共 -", sum(count),"次")
```
### 16.8
```python=
import random

color_balls = ['red', 'yellow', 'black', 'green', 'orange']
black_count = 0
for i in range(0,100):
    picked_balls = random.sample(color_balls, 2)
    if "black" in picked_balls:
        black_count+=1
print("挑中黑色球的次數:", black_count, "次")
```
### 16.9
```python=
import random

color_balls = ['red', 'yellow', 'black', 'green', 'orange']
black_count = 0
for i in range(0,100):
    random.shuffle(color_balls)
    picked_balls = random.sample(color_balls, 2)
    if "black" in picked_balls:
        black_count+=1
print("挑中黑色球的次數:", black_count, "次")
```
### 16.10
原本的程式碼
```python=
import random
scores = []

for c1 in range(65, 91):
    for c2 in range(65, 91):
        name = chr(c1) + chr(c2)
        score1 = random.randint(0, 100)
        score2 = random.randint(0, 100)
        score3 = random.randint(0, 100)
        scores += [(name, score1, score2, score3)]
```
修改後的程式碼
```python=
import random
scores = []

for c1 in range(65, 75):
    for c2 in range(65, 91):
        for c3 in range(65, 91):
            name = chr(c1) + chr(c2) + chr(c3)
            score1 = random.randint(0, 100)
            score2 = random.randint(0, 100)
            score3 = random.randint(0, 100)
            scores += [(name, score1, score2, score3)]
```

執行時間差: 修改後慢大約 0.024秒(修改前的10倍)

### 16.11

```python=
import random
scores = []

for c1 in range(65, 76):
    for c2 in range(65, 91):
        for c3 in range(65, 91):
            name = chr(c1) + chr(c2) + chr(c3)
            score1 = random.randint(0, 100)
            score2 = random.randint(0, 100)
            score3 = random.randint(0, 100)
            scores += [(name, score1, score2, score3)]

sum = []
for i, item in enumerate(scores):
    sum += [item[1] + item[2] + item[3]]

for j in range(len(sum)):
    for k in range(len(sum)):
        if sum[k] < sum[j]:
            sum[k], sum[j] = sum[j], sum[k]
            scores[k], scores[j] = scores[j], scores[k]

for l, item in enumerate(scores):
    print(l ,item, '總分', item[1] + item[2] + item[3])
```