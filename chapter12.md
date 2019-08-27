# chapter12
### 12.1
```python=
x = [i for i in range(1,11)]
```
### 12.2
```python=
good_score = [item for item in scores if item>=90]
```
### 12.3
```python=
divide_by_ten = [i/10 for i in range(1,11)]
```
### 12.4
>[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
### 12.5
>[(1, 'a'),(1, 'b'),(1, 'c'),(2, 'a'),(2, 'b'),(2, 'c'),(3, 'a'),(3, 'b'),(3, 'c')]
### 12.6
```python=
exclude_multiples_of_six = [i for i in range(1,101) if i % 2 == 0 and i % 6 != 0]
```
    

### 12.7
```python=
num_list = [i for i in range(1,101) if i % 2 == 0 and i % 6 != 0] 

for i in enumerate(num_list, start=1):
    print(i, end=' ') #不要換行
```
### 12.8 
> 4，只會取到前一項
### 12.9
```python=
num_list = [n for n in range(1,101)]

#一般for迴圈
num_list_copy1 = []
for i in range(0,len(num_list)):
    num_list_copy1 += [num_list[i]]
    
#單行for迴圈
num_list_copy2 = [j for j in num_list]
    
#Slice
num_list_copy3 = num_list[:]
```
### 12.10
```python=
#接續上題
    
#單行for迴圈
num_list_copy4 = num_list[::3]
    
#Slice
num_list_copy5 = [j for i,j in enumerate(num_list) if i % 3 == 0]
```
### 12.11
```python=
#接續12.9
#一般迴圈
num_list_reverse1 = [] 
for i in range(len(num_list)-1,-1,-1):
    num_list_reverse1 += [num_list[i]]
        
#Slice
num_list_reverse2 = num_list[::-1]
```