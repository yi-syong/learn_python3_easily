# Chapter 21


### 21.1
`3`
### 21.2
`def`
### 21.3
`return`
`return`
### 21.4
```python=
def find_max(list_of_nums):
    return max(list_of_nums)
```
### 21.5
```python=
def modify_scores(list_of_scores):
    for i in range(len(list_of_scores)):
        if 55 <= list_of_scores[i] < 60:
            list_of_scores[i] = 60

    print(list_of_scores)

scores = [90, 75, 55, 80, 57, 60]
modify_scores(scores)
```