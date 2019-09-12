import random

color_balls = ['red', 'yellow', 'black', 'green', 'orange']
black_count = 0
for i in range(0,100):
    random.shuffle(color_balls)
    picked_balls = random.sample(color_balls, 2)
    if "black" in picked_balls:
        black_count+=1
print("挑中黑色球的次數:", black_count, "次")