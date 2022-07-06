arr = [1,4,3,2,6,7]
n = len(arr)
i = arr[0]
count = 0
while i<n:
    count =count+1
    i = i+arr[i]
print(count+1)