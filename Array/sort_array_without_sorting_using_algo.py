# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
a = [0,1,1,0,0,2,0,2,1,0,0]
low = 0
mid = 0 
high = len(a) - 1

while(mid <= high):
    if a[mid] == 0:
        a[mid], a[low] = a[low], a[mid]
        mid = mid + 1
        low = low + 1
    elif a[mid] == 1:
        mid = mid + 1
    else:
        a[mid], a[high] = a[high], a[mid]
        high = high - 1

print(a)