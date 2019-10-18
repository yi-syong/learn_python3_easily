# Chapter 4


### 4.1
`3`
### 4.2
`import turtle as tu`
### 4.3
`help`
### 4.4
`1`
### 4.5
`3`
### 4.6
`4`
### 4.7
```python=
import turtle as tu
tu.showturtle()
tu.color('red')
tu.pensize('5')
tu.goto(150, 150)
tu.goto(0, 300)
tu.goto(-150, 150)
tu.goto(0, 0)
```
### 4.8
```python=
import turtle as tu
tu.showturtle()
tu.color('blue')
tu.pensize('5')
tu.penup()
tu.goto(50, 0)
tu.pendown()
tu.goto(200, 0)
tu.goto(200, 150)
tu.goto(50, 150)
tu.goto(50, 0)

tu.penup()
tu.goto(-50, 0)
tu.pendown()
tu.goto(-200, 0)
tu.goto(-200, 150)
tu.goto(-50, 150)
tu.goto(-50, 0)
tu.right(90) #看起來才跟圖一樣XD
```
### 4.9
`color`
`circle`
### 4.10
`right`
`pensize`
`forward`
### 4.11
```python=
import turtle as tu

tu.showturtle()
tu.circle(100, 360, 3)

tu.penup()
tu.goto(0, 200)
tu.pendown()
tu.right(180)
tu.circle(100, 360, 3)
```
### 4.12
```python=
import turtle as tu

tu.showturtle()
tu.circle(50)
tu.penup()
tu.goto(50, 0)
tu.pendown()
tu.circle(50)
tu.penup()
tu.goto(100, 0)
tu.pendown()
tu.circle(50)
tu.penup()
tu.goto(150, 0)
tu.pendown()
tu.circle(50)
```