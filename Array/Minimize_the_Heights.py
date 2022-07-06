arr = [2,6,3,4,7,2,10,3,2,1]
k = 5
n = len(arr)
arr.sort()
ans = arr[n-1] - arr[0]
smallest = arr[0] + k
largest = arr[n-1] - k


for i in range(n-1):
    if arr[i] >=k:
        mini = min(smallest,arr[i+1]-k)
        maxi = max(largest, arr[i]+k)
        ans = min(ans,maxi-mini)

print(ans)