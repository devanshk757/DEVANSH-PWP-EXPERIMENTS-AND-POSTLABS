t1 = (1, 2, 3)
print(t1)

l1 = [1, 2, 3]
print(l1)

l1[0] = 4
print(l1)

t2 = (2, 3, 4, 5, 6, 7)
t3 = (4, 5, 6, 7, 8)
print(t2 + t3)

import numpy as np
t2 = (1, 2, 3)
t3 = (4, 5, 6)
print(tuple(np.array(t2) + np.array(t3)))

print(t2[0] + t3[0])

t2 = (1, 3, 4, 5, 6, 7, 8)
t3 = (7, 8, 9, 10, 11, 12)
print(t2[1:4])
print(t2[1:4:2])
print(t2[1:4] + t3[1:4])
print(t2[1:4] + t2[1:4])
print(2 * t2[1:4])
print(type(t2))

print(tuple(range(5)))
print(tuple(range(1, 8)))
print(tuple(range(1, 8, 2)))
print(tuple(range(10, 2, -1)))

t1 = (1, 2, "A", 5)
print(t1)

t1 = (1, 2, "A" "B", 5, 7)
print(t1)
print(len(t1))

t1 = (2, 3, 4, 5)
print(sum(t1))

t1 = (2, 3, 4, 5, 7)
print(sum(t1))

t1 = (2, 3, 4, 5)
print(min(t1))
print(max(t1))

t1 = (2, 3, 4, 5, 6, 3)
print(t1.count(9))
print(t1.index(3))


a = (5,6,7,5,5,9,7)
b = ("a","b","v","b")
my_tu_1 = tuple(dict.fromkeys(a)) 
print(my_tu_1)
my_tu_2 = tuple(dict.fromkeys(b)) 
print(my_tu_2)

first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime') 
last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes') 
ages = (49, 55, 39, 33)
zipped = tuple(zip(first_names, last_names,ages)) 
print(zipped)
