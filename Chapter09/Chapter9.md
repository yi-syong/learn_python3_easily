# Chapter 9


### 9.1
```
exam_pass = False if score < 60 else True
```
### 9.2
```
result = "奇數" if num % 2 != 0 else "偶數"
```
### 9.3
```
is_adulthood = "成年" if age >= 18 else "未成年"
```
### 9.4
```python=
score1 = int(input("輸入第一科考試成績:"))
score2 = int(input("輸入第二科考試成績:"))
score3 = int(input("輸入第三科考試成績:"))

if score1 < 60 or score2 < 60 or score3 < 60:
    print("有成績不及格")

else:
    print("全部及格")
```

### 9.5
```python=
num = int(input("請輸入一個整數:"))
is_common_multiple = "是7與13的公倍數" if num % 7 == 0 and num % 13 == 0 else "不是7與13的公倍數"
print(is_common_multiple)
```

### 9.6
```python=
num = int(input("請輸入一個整數:"))

if num % 7 == 0 and num % 13 == 0:
    print("是7與13的公倍數")
    
elif num % 7 == 0:
    print("是7的倍數，但不是13的倍數")

elif num % 13 == 0:
    print("是13的倍數，但不是7的倍數")

else:
    print("不是7與13的公倍數")
```
### 9.7
```python=
year = int(input("請輸入西元年:"))

if year % 4 == 0 and year % 100 != 0:
    print("閏年")
elif year % 400 == 0:
    print("閏年")
else:
    print("平年")
```