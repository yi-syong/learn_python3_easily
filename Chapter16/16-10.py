start = time.clock()
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
end = time.clock()

print (end-start)