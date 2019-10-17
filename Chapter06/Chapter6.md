# Chapter 6


### 6.1
`4`
### 6.2
`3`
### 6.3
```
'李大中' 90

name 'name' is not define
```
### 6.4
`1`
### 6.5
`4`
### 6.6
`3`
### 6.7
`1`
### 6.8
`2`
### 6.9
`3`
### 6.10
`3`
### 6.11
```python=
miles = 40076*0.623
print('繞赤道一圈需要:', miles / 470, '小時')
print('若在24小時內繞完，時速為:', miles / 24, '英哩')
```
### 6.12
```python=
c1 = 2-8j
c2 = 1+5j

print(c1, '+', c2, '=', c1 + c2)
print(c1, '-', c2, '=', c1 - c2)
print(c1, '*', c2, '=', c1 * c2)
print(c1, '/', c2, '=', c1 / c2)
```
### 6.13
```python=
import decimal as de
square_root_2 = de.Decimal(2**0.5)
de.getcontext().prec = 100
print(square_root_2)
```