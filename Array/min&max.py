# Maximum and minimum of an array 
a = [21,2,3,4,5,6,7,8]
min = a[0]
max = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i] 
print("max element array: ", max)
print("min element array: ", min)

