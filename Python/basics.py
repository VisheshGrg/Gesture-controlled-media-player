print("Hello World")
print(100)

# this is the quotient operator 
print(3//4)

# _42 using this _42 acts as a variable
_42 = "Hello world"
print(_42)

# concatinates the string to itself
x = 'h'
x*=2
print(x)

arr = ['vishesh', 43, '2', [23,21]];
print(arr);
# prints the array from backward 
print(arr[-1]);

# 3 is not included
print(arr[0:3]);

# 2 is the step here it means it will jump 2 steps and index 12 is not included
print(arr[0:12:2]);

listA = [1,2,3,4,5,6,7,8,9,10]
# -1 is the inverted step
print(listA[::-1])

#prints the whole list
print(listA[::])

inp = input()
print(inp)
inp = int(inp)
print(inp)
inp = str(inp)

print(listA[::2] + listA[::-2])
print(listA[1::2] * 2)
print((listA[0:2] + listA[1::-1])*2)

# tuple 
# tuple is different from list as elements cant be changed in tuple but it is possible in list
tpl = (1,2,"ram",4,5);
print(tpl)
#gives error
# tpl[2] = "ram"
#other feature

x,y = (1,"ram");
print(y);
# gives value of x as 1 and value of y as 2
# x,y = (1,2,4) gives error 

#dictionary
obj = {
    "name" : "Vishesh",
    "age" : 18,
    "branch" : "IT"
}

print(obj["name"]);

obj2 = {
    'cars': ['red','orange','pink'],
    'num' : 1,
    x: 'temp'
}
print(obj2['cars'])
print(obj2[x])



