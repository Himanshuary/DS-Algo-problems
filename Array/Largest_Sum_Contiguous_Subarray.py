# Appoarch1 : Brute force 

arr = [1,2,3,-2,5]
max_sum = 0
n = len(arr)
for i in range(n):
    current_sum = 0
    for j in range(i,n):
        current_sum = current_sum + arr[j]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)

# Appoarch2 : Kadane’s Algorithm

max = 0
current = 0
for i in range(n):
    current = current + arr[i]
    if current > max:
        max = current 
    if current < 0:
        current = 0
print("Kadane’s Algorithm solution: ", max)