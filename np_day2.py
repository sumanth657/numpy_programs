import numpy as np
x=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in x:
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)


