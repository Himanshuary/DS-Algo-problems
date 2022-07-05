from re import M


a = [1,2,3,4,5,6,7]
b = [1,2,3,8,9,8,0]
n = len(a)
m = len(b)
sum = n + m

if n<m:
    max = m
else:
    max = n

c = 0
for i in range(max):
    if a[i] == b[i]:
        c = c+1

print(sum-c)