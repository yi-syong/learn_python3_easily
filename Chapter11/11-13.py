num_student = int(input("請輸入學生人數:"))

score_list = []
for i in range(0, num_student):
    score = int(input("請輸入學生成績:"))
    score_list += [score]

pass_count = 0
fail_count = 0
for item in score_list:
    if item >= 60:
        pass_count += 1
    if item < 60:
        fail_count += 1

print("及格學生人數:", pass_count)
print("不及格學生人數:", fail_count)