scores = input('請輸入國、英、數三科成績，成績之間加入空格:').split()
ch_score = float(scores[0])
en_score = float(scores[1])
math_score = float(scores[2])

#不用and的話要再一層if ...
if ch_score > en_score and ch_score > math_score:
    if en_score > math_score:
        print('國文:', ch_score)
        print('英文:', en_score)
        print('數學:', math_score)
    else:
        print('國文:', ch_score)
        print('英文:', en_score)
        print('數學:', math_score)
        
if en_score > ch_score and en_score > math_score:
    if ch_score > math_score:
        print('英文:', en_score)
        print('國文:', ch_score)
        print('數學:', math_score)
    else:
        print('英文:', en_score)
        print('數學:', math_score)
        print('國文:', ch_score)
        
if math_score > en_score and math_score > ch_score:
    if en_score > ch_score:
        print('數學:', math_score)
        print('英文:', en_score)
        print('國文:', ch_score)
    else:
        print('數學:', math_score)
        print('國文:', ch_score)
        print('英文:', en_score)