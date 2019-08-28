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