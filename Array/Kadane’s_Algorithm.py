arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max = arr[0]
current = 0
n = len(arr)
for i in range(n):
    current = current + arr[i]
    if current > max:
        max = current 
    if current < 0:
        current = 0
print("Kadane’s Algorithm solution: ", max)