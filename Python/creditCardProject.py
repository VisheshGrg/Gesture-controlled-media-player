
# i = 0;
# cardNumber = '1234567890123456'
# while 1==1:
#     if i<12:
#         print('x')
#     elif i>=12 and i<16:
#         print(cardNumber[i])
#     else:
#         break
#     i +=1

def func(x):
    decodedNum = ""
    for i in range(0,16):
        if i>11:
            decodedNum += x[i]
        else:
            decodedNum += 'x'
    return decodedNum

x="1234567898765432"

print(func(x))
