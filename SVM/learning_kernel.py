import numpy as np
import math as m

x1 = np.array([1,2,3,4,5])
x2=np.array([6,7,8,9,10])


def map(array):
    v = [a for a in array]
    v.append(array[1]*array[2] )
    v.append(array[3]**2)
    v.append(array[2]**2 * array[4])
    return np.array(v)

map_result = (np.dot(map(x1), map(x2)))
print(map_result)

print (m.log(map_result,np.dot(x1,x2)+1))


print((np.dot(x1,x2)+1)**2.1183784)



x3 = np.array([7,2,8,4,5])
x4=np.array([1,7,4,2,10])
map_result2 = (np.dot(map(x3), map(x4)))
print(map_result2)
print((np.dot(x3,x4)+1)**2.1183784)