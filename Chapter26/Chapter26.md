# Chapter 26


### 26.1
`2`
### 26.2
`3`
### 26.3
`4`
### 26.4
`2`
### 26.5
`3`
### 26.6
`Circle`
`get_area()`
`get_perimeter()`
### 26.7
1. 在 shape 資料夾新增 `rect.py`
2. 在 `rect.py` 加入以下程式碼
```python=
class Rect:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_area(self):
        return self._length * self._width
    
    def get_perimeter(self):
        return 2 * (self._length + self._width)
```
4. `__init__.py` 加入 `from shape.rect import *`
5. 測試 Rect 類別的功能