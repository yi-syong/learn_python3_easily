import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = set(random.sample(letters, 10))
t = set(random.sample(letters, 10))
u = set(random.sample(letters, 10))

print('沒有被挑到的字母:', set(letters)-(s | t | u))
print('被挑到一次的字母:', (s ^ t ^ u)-(s & t & u))
print('被挑到兩次的字母:', ((s & t)|(t & u)|(s & u))-(s & t & u))
print('被挑到三次的字母:', s & t & u)