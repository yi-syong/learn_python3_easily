# Chapter 13

### 13.1
> 3，可以不同 
### 13.2
```python=
class1_score_list = [70, 80, 90, 100]
class2_score_list = [100, 90, 80, 70]
class3_score_list = [80, 90, 80, 90]

all_score_list = [class1_score_list, class2_score_list, class3_score_list]
```
### 13.3
```python=
#接續上一題
class_num = int(input('請輸入學生班級：'))-1
student_num = int(input('請輸入學生編號：'))-1
print("該同學成績:", all_score_list[class_num][student_num])
```
### 13.4
```python=
num_class = int(input('總班級數:'))

all_score_list = []
for i in range(0, num_class):
    print('第', i+1, '班 ------------')
    num_student = int(input('學生人數:'))
    score_list = []
    for j in range(0, num_student):
        score = int(input('請輸入學生成績'))
        score_list += [score]
        
    all_score_list += [score_list]
    
grade_A_count = []
grade_B_count = []
grade_C_count = []
grade_D_count = []
grade_E_count = []

for score_list in all_score_list:
    
    A_count = 0
    B_count = 0
    C_count = 0
    D_count = 0
    E_count = 0
    
    for score in score_list:
        if 100>=score>=90:
            A_count += 1
        if 90>score>=80:
            B_count += 1
        if 80>score>=70:
            C_count += 1
        if 70>score>=60:
            D_count += 1
        if score<60:
            E_count += 1
    
    grade_A_count += [A_count]
    grade_B_count += [B_count]
    grade_C_count += [C_count]
    grade_D_count += [D_count]
    grade_E_count += [E_count]

for i in range(0, len(grade_A_count)):
    print('第', i+1, '班------------',)
    print('等級A人數:', grade_A_count[i])
    print('等級B人數:', grade_B_count[i])
    print('等級C人數:', grade_C_count[i])
    print('等級D人數:', grade_D_count[i])
    print('等級E人數:', grade_E_count[i])
```

### 13.5
```python=
school_score_list = []
for i in range(0, 6):
    print(i+1, '年級************')
    num_class = int(input('班級數:'))
    grade_score_list = []
    for j in range(0, num_class):
        print('第', j+1, '班 ------------')
        num_student = int(input('學生人數:'))
        score_list = []
        for k in range(0, num_student):
            score = int(input('請輸入學生成績'))
            score_list += [score]
        grade_score_list += [score_list]
    school_score_list += [grade_score_list]
    
print(school_score_list)
```

### 13.6

<p> enumerate </p>

### 13.7
```python=
print('請輸入10筆學生成績')
score_list = []
for i in range(1,11):
    score = int(input('請輸入學生成績:'))
    score_list += [score]
    
print('不及格的成績-----------------')

for i, score in enumerate(score_list):
    if score < 60:
        print('學號:', i+1, '成績:', score)
```

### 13.8
```python=
print('請輸入10筆學生成績')
score_list = []
for i in range(1,11):
    score = int(input('請輸入學生成績:'))
    score_list += [score]

print('所有的成績-----------------')

for i, score in enumerate(score_list):
    if 60>score>=55:
        score = 60
    print('學號:', i+1, '成績:', score)
```
