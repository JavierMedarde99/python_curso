mi_set = set([1,2,3,(2,3,4),4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3,1,1,1,2,2}
print(type(otro_set))
print(otro_set)
print(len(otro_set))
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s1.add(4)
s1.add(2)
s1.remove(3)
s1.discard(6)
s1.pop()
s1.clear()
print(s1)
