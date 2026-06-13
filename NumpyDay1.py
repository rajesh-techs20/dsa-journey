import numpy as np
a=np.array([1,2,3])
print(a)
print(a+2)
print(a*2)
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))

b=np.array([5,10,15,20,25])

print(b)
print(b+10)
print(b*3)
print(np.sum(b))
print(np.mean(b))

#2D ARRAY
import numpy as np
matrix=np.array([
    [1,2,3],
    [4,5,6]
])
print(matrix)
print(matrix.shape)
print()
print(matrix[0][0])
print(matrix[1][2])
