# Chapter 23


### 23.1
`4`
### 23.2
`import`
`paint`
`paint`
### 23.3
`3`
### 23.4
`4`
### 23.5
`game.paint`
`pt`
`pt`
### 23.6
```python=
import scoprocess as sp

scores = [80, 95, 70, 40, 65, 55, 75, 50, 90]
print('最高分:', sp.scocheck.highest(scores))
print('最低分:', sp.scocheck.lowest(scores))
print('平均分數:', sp.scocheck.average(scores))
print('及格:', list(sp.scocheck.get_pass_scores(scores)))
print('不及格:', list(sp.scocheck.get_fail_scores(scores)))

print('由低到高排序:', sp.scosort.sort_low_to_hight(scores))
print('由高到低排序:', sp.scosort.sort_high_to_low(scores))

#not sure
```
