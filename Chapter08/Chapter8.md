# Chapter 8


### 8.1
```
en_score > ch_score
```
### 8.2
```
ch_score > en_score > math_score
```
### 8.3
```
ch_score > math_score < en_score
```
### 8.4
```
ch_score > 90
ch_score - en_score > 20
```
### 8.5
```python=
if 0 <= score < 60:
    print('成績不及格')
elif 60 <= score <= 100:
    print('成績及格')
else:
    print('分數錯誤')
```
### 8.6
```python=
scores = input('請輸入國、英、數三科成績，成績之間加入空格:').split()
ch_score = float(scores[0])
en_score = float(scores[1])
math_score = float(scores[2])

#不用and的話要再一層if ...
if ch_score > en_score and ch_score > math_score:
    if en_score > math_score:
        print('國文:', ch_score)
        print('英文:', en_score)
        print('數學:', math_score)
    else:
        print('國文:', ch_score)
        print('英文:', en_score)
        print('數學:', math_score)
        
if en_score > ch_score and en_score > math_score:
    if ch_score > math_score:
        print('英文:', en_score)
        print('國文:', ch_score)
        print('數學:', math_score)
    else:
        print('英文:', en_score)
        print('數學:', math_score)
        print('國文:', ch_score)
        
if math_score > en_score and math_score > ch_score:
    if en_score > ch_score:
        print('數學:', math_score)
        print('英文:', en_score)
        print('國文:', ch_score)
    else:
        print('數學:', math_score)
        print('國文:', ch_score)
        print('英文:', en_score)
```

### 8.7
```python=
num_str = input('請輸入小於100000的整數:')

if 0 < int(num_str) < 100000:
    print(len(num_str),'位數')
else:
    print('輸入錯誤')
```
### 8.8
```python=
if gender == '男':
    if age > 35:
        print('趕快結婚')
    elif 35 >= age >= 30:
        print('已達適婚年齡')
    else:
        print('未達適婚年齡')
        
else:
    if age > 30:
        print('趕快結婚')
    elif 30 >= age >= 25:
        print('已達適婚年齡')
    else:
        print('未達適婚年齡')
```
### 8.9
```python=
if student == 'A':
    if 90 <= score <= 100:
        print('A級')
    elif 90 > score >= 80:
        print('B級')
    elif 80 > score >= 70:
        print('C級')
    elif 70 > score >= 60:
        print('D級')
    elif 60 > score:
        print('E級')
    else:
        print('輸入錯誤')
        
else:
    if 85 <= score <= 100:
        print('A級')
    elif 85 > score >= 75:
        print('B級')
    elif 75 > score >= 65:
        print('C級')
    elif 65 > score >= 55:
        print('D級')
    elif 55 > score:
        print('E級')
    else:
        print('輸入錯誤')
```
