# Chapter 27


### 27.1
`1`
### 27.2
`2`
### 27.3
`4`
### 27.4
`3`
### 27.5
`3`
### 27.6
`4`
### 27.7
`teacher.py`

```python=
class Teacher:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def get_data(self):
        return self._name, self._age

##沒有確認年齡輸入是否為數字
```

`classroom.py` **修改部分**

```python=
    def __init__(self):
        self._students = []
        self._teacher = []

    def get_teacher(self):
        return self._teacher
```

`main.py` **修改部分**
```python=
#修改function
def show_students(classroom1, classroom2):
    print('教室一的老師:')
    for s in classroom1.get_teacher():
        print(s.get_data())
    print('第一間教室:')
    for s in classroom1.get_all_students():
        print(s.get_data())
    print('教室二的老師:')
    for s in classroom2.get_teacher():
        print(s.get_data())
    print('第二間教室:')
    for s in classroom2.get_all_students():
        print(s.get_data())

#新增兩位老師
teacher1 = ca.Teacher('老師一號', 20)
teacher2 = ca.Teacher('老師二號', 80)

#把老師分給教室1跟2
print('-----student in class-----')
classroom1.set_teacher(teacher1)
classroom1.add_student(student1)
classroom1.add_student(student2)
classroom1.add_student(student3)

classroom2.set_teacher(teacher2)
classroom2.add_student(student4)
classroom2.add_student(student5)

#剩下都一樣
```