# Appoarch1 : using sorting
a = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
a.sort()
print(a)
# Time complexity: O(nlog(n))

# Appoarch2: partition process
arr = [1, -2, -3, 4, 5, -6, 7, 8, -9]
pivot = arr[0]
j = 0

n = len(arr)
for i in range(n):
    if arr[i] < 0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j = j+1
print(arr)