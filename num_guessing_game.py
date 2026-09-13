import random
sn = random.randint(1, 100)
a = 0
gn = int(input("Guess the num btwn 1 t0 100 :"))
while sn != gn:
    if gn>sn:
        print("Too high!")
    elif gn<sn:
        print("Too low!")
    gn = int(input("Guess the num btwn 1 t0 100 :"))
    a += 1
else:
    print("PERFECT! \n You done it in ",a ,"attempts")
    


