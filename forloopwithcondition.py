for i in range (1,11):
    if i % 2 == 0:
        print(i,"is even")
    else:
        print(i,"is odd")



#multiply of 3
for i in range(1,21):
    if i % 3 == 0:
        print(i,"is divisible by 3")
    else:
        print(i,"is not divisble by 3")


#nested condition inside for
for i in range(1,16):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"fizzbuzz")
    elif i % 3 == 0:
        print(i,"fizz")
    elif i % 5 == 0:
        print(i,"buzz")
    else:
        print(i)
