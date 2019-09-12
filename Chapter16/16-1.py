#由小到大排序

sorted_scores = []
scores = [60, 10, 90, 100, 20, 30, 80, 50, 40, 70]
for i in range(0, len(scores)):
    min_score = max(scores)
    min_score_index = 0
    for j, data in enumerate(scores):
        if data < min_score:
            min_score = data
            min_score_index = j
            
    lowest_score = scores.pop(min_score_index)
    sorted_scores += [lowest_score]