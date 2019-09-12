import random

dice_num = []
for i in range(0,100):
    random_num = random.randint(1,6)
    dice_num += [random_num]

count = [0 for i in range(0,6)]
for j, point in enumerate(dice_num):
    if point == 1:
        count[0]+=1
    if point == 2:
        count[1]+=1
    if point == 3:
        count[2]+=1
    if point == 4:
        count[3]+=1
    if point == 5:
        count[4]+=1
    if point == 6:
        count[5]+=1

print("1點 -", count[0], "次")
print("2點 -", count[1], "次")
print("3點 -", count[2], "次")
print("4點 -", count[3], "次")
print("5點 -", count[4], "次")
print("6點 -", count[5], "次")
print("總共 -", sum(count),"次")