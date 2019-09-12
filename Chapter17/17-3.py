#智商不夠只好這樣寫
while True:
    try:
        a,b,c = input('請輸入三個正整數:').split()
        if int(a)>0 and int(b)>0 and int(c)>0:
            a = int(a)
            b = int(b)
            c = int(c)
            break
        else:
            print("輸入錯誤，請重新輸入")
    except:
        print("輸入錯誤，請重新輸入")

if a < b:
    a, b = b, a

r1 = a % b
while r1 != 0:
    a = b
    b = r1
    r1 = a % b

if b < c:
    b, c = c, b

r2 = b % c
while r2 != 0:
    b = c
    c = r2
    r2 = b % c

print('GCD is', c)