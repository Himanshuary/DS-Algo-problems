from array import*
# 1st method
print("first method")

def reverse(arr,l,r):
    while l<r:
        arr[l],arr[r] = arr[r],arr[l]
        l=l+1
        r=r-1
    return arr
#a = list(map(int, input().split()))
a = [1,2,3,4,5]
n = len(a)
r = n-1
print(reverse(a,0,r))

# second method
print("second method--")
a = a[::-1]
print(a)

#third method
print('Third method')
arr1 = array('i', [1,2,3,4,5])
arr1.reverse()
print(arr1)