# Chapter 7


### 7.1
`input`
### 7.2
`int(input('請輸入年齡'))`
### 7.3
`float(input('請輸入身高'))`
### 7.4
`3`
### 7.5
`split`
`float`
### 7.6
```python=
name, age, height = input('請輸入姓名、年齡及身高，資料間請加入空格').split()
age = int(age)
height = float(height)

print('姓名:', name)
print('年齡:', age)
print('身高:', height)
```
### 7.7
`37`
`26`
`12`
### 7.8
```python=
base, height = input('請輸入三角形的底和高，之間請加入空格:').split()
base, height = float(base), float(height)

print('三角形面積 =', base * height / 2)
```
### 7.9
```python=
from math import pi

radius = input('請輸入半徑:')
radius = float(radius)

print('圓的面積為:', pi * radius**2)
```
### 7.10
```python=
a, b, c = input('請輸入一元二次方程式的係數a、b及c的值，之間請加入空格:').split()
a, b, c = int(a), int(b), int(c)

print('x的解為:', (-b + (b**2 - 4*a*c)**0.5) / (2*a), '以及', (-b - (b**2 - 4*a*c)**0.5) / (2*a))
```
### 7.11
```
result1 += 5*value1 - value2 
result2 -= 5*value1 / value2 
result3 *= value1 * 30.5
result4 **= 2
result5 %= 7 
```