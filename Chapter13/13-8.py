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