import numpy as np 
#my name is sumanth
# x=np.array([1,2,3,4,6,7])
# print(x)
# y=x.copy()
# y[0]=100
# print(y)
# print(x.shape)
# print(x.ndim)
#converting from 1d to 2d..,
# y=x.reshape(3,2)
# print(y)
# x=np.([10,11,12,13,14,15,16,17])
#1d to 3d
# y=x.reshape(2,2,2)
# print(y)
# y=[]

# for i in range(len(x)):
#     if (x[i]%3)==0:
#        x[i]=100
# print(x)
    # print(i)
# x=np.array([[10,11,12,13,15],[16,17,18,19,20]])
# for i in x:
#     print(i)
#     for j in i:
#         print(j)
x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in x:
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)
