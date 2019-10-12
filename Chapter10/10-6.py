import random as rand

for i in range(0, 3, 1):
    rand_num1 = rand.randint(0,1)
    rand_num2 = rand.randint(0,1)
    
    if rand_num1 + rand_num2 == 1:
        print("聖筊")
    else:
        print("失敗")
        break

else:
    print("連續三個聖筊")