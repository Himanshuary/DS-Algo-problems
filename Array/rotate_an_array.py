arr = [1, 2, 3, 4, 5]
k= 2
for i in range(k):
    temp = arr.pop()
    arr.insert(0,temp)
print(arr)