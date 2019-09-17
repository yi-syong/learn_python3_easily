# Chapter 18

### 18.1
>1

### 18.2
>4

### 18.3
以上皆非，空白鍵的 ASCII code 最小...

### 18.4
>4

### 18.5
>3

### 18.6
>4

### 18.7
>1

### 18.8
> 1 & 4

### 18.9
>3

### 18.10
>2

### 18.11
>1

### 18.12
>4

### 18.13
>4
>
### 18.14
>2

### 18.15
```python=
nums_str = input('請輸入三個數，數字之間加入空格:').split()
nums = []

while True:
    for n in nums_str:
        deciaml_pnt_postition = n.find('.')
        
        if deciaml_pnt_postition > 0:
            int_part = n[:deciaml_pnt_postition]
            deciaml_part = n[deciaml_pnt_postition + 1:]
            if int_part.isdigit() and deciaml_part.isdigit():
                nums += [float(n)]

        if n.isdigit():
            nums += [int(n)]
        if len(nums) == 3:
            break;

    if len(nums) < 3:
        nums_str = input('請繼續輸入').split()
    else:
        break;

print(nums)
```