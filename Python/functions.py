def myFunc(x):
    y = x*2
    print(y)
    if False:
        return x + 23.323
    print("This part will execute!")
    return (x+20, 5)

num = 10
print(num)
x,y = myFunc(num)
print(x,y)  


