arr = [7,1,5,3,6,4]
max = 0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j] - arr[i] > max:
            max = arr[j] - arr[i]
        elif max <= 0:
            print(0)
print(max)