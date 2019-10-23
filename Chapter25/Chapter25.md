# Chapter 25


### 25.1
`3`
### 25.2
`4`
### 25.3
`2`
### 25.4
`at`
`write`
### 25.5
`2`
### 25.6
`3`
### 25.7
`with`
`as`
`for`
### 25.8
```python=
import os

FILE = 'D:\\data.bin'

if os.path.isfile(FILE):
    print('錯誤:' + FILE + '已經存在')
    exit()

with open(FILE, 'w+b') as file:
    for i in range(1, 10001):
        int_bytes = i.to_bytes(4, 'big')
        file.write(int_bytes)
    
    file.seek(0)
# file size: 40kB
```
### 25.9
```python=
import os

FILE = 'D:\\data.txt'

if os.path.isfile(FILE):
    print('錯誤:' + FILE + '已經存在')
    exit()

with open(FILE, 'w+t') as file:
    for i in range(1, 10001):
        file.write(str(i) + '\n')
    
    file.seek(0)
    
# file size: 58kB
```
### 25.10

1. 增加一個地址欄位
```python=
# 只顯示修改部分

# friend.py
def add(file, name, gender, age, tel, addr):
    if gender == 1:
        gender = '男'
    else:
        gender = '女'

    line = name + ' ' + gender + ' ' + str(age) + ' ' + tel + ' ' + addr + '\n'
    file.write(line)

# main.py
    if op == '1':
        try:
            name, gender, age, tel, addr = input(
                '請輸入朋友姓名、性別(1男生、2女生)、年齡、電話、地址'
                + '，資料用空白分隔 \n'
            ).split()

            gender = int(gender)
            age = int(age)
        except ValueError:
            print('資料格式錯誤 \n')
        else:
            fr.add(file, name, gender, age, tel, addr)
            print('加入成功 \n')
```

2. 新增用電話搜尋的選項

```python=

# friend.py
def find_by_tel(file, tel):
    file.seek(0, 0)
    friend_data = []
    for line in file:
        name, gender, age, tel_this_line, address = line.split()
        if tel_this_line == tel:
            friend_data += [name, gender, age, tel_this_line, address]
            return friend_data

# main.py
    elif op == '5': #可自行調整功能順序
        tel = input('input tel \n')
        friend_data = fr.find_by_tel(file, tel)

        if not friend_data:
            print('not found')
        else:
            print(friend_data, '\n')

```

 - P.S. 這樣寫的缺點是只能找出第一筆一樣的~


3. 新增一個清除通訊錄的選項
```python=

# friend.py
def clean_friends():
    os.remove(DATA_FILE)
    
# main.py
    elif op == '6':
        fr.clean_friends()
```