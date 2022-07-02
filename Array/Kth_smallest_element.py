a = [7,10,4,3,20,15]
k = 2
n = len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print("The Kth smallest element: ", a[k-1])