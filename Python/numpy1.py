import numpy as np

# # numpy array is homogenious
# # 1-d array
# a = np.array([1,2,3]);
# print(a)
# print(type(a))
# print(a.size)
# print(a.ndim)
# print(a[0])

# # 2-d array 
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b)
# print(b[0][1])
# # or 
# print(b[0,1])
# print(b.shape)

# c = np.array([1,2,3,4,5,6])
# # converts it into 2*3 matrix but only possible if the elements are complete 
# d = c.reshape(2,3)
# print(c)
# print(d)

# print(" ")

# e = np.array([[1,2,3],[4,5,6]])
# f = e.reshape(3,2)
# print(e)
# print(f)

# g = np.ones([3,3])
# print(g)

# h = np.zeros([3,3])
# print(h)    

# print(" ")

# i = np.arange(5)
# print(i)

# j = np.full((10,10),0)
# print(j)

# identitymatrix = np.eye(3)
# print(identitymatrix)

# randomMatrix = np.random.random((3,3))
# print(randomMatrix)

# a = np.full((5,5),1)
# a[1:4,1:4] = 0
# a[2:3,2:3] = 9
# print(a)

# b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(b[-1,-4:-1])

a = np.array([1,2,3])
# b = a
# any changes in b reflects changes in a
# b[0] = 8
# print(a[0])

# to make separate copies
b = a.copy()
b[0] = 8
print(a[0])
print(b[0])

c = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(np.add(a,b))
print(np.subtract(a,b))
print(np.divide(a,b))
print(np.power(a,b))
print(np.sqrt(a))

print(c.T) # for transpose
print(np.sum(c))
print(np.sum(c,axis=0)) #col wise sum
print(np.sum(c,axis=1)) #row wise sum






