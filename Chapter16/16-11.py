import random
scores = []

for c1 in range(65, 76):
    for c2 in range(65, 91):
        for c3 in range(65, 91):
            name = chr(c1) + chr(c2) + chr(c3)
            score1 = random.randint(0, 100)
            score2 = random.randint(0, 100)
            score3 = random.randint(0, 100)
            scores += [(name, score1, score2, score3)]

sum = []
for i, item in enumerate(scores):
    sum += [item[1] + item[2] + item[3]]

for j in range(len(sum)):
    for k in range(len(sum)):
        if sum[k] < sum[j]: #由大至小排序
            sum[k], sum[j] = sum[j], sum[k]
            scores[k], scores[j] = scores[j], scores[k]

for l, item in enumerate(scores):
    print(l ,item, '總分', item[1] + item[2] + item[3])