from audioop import reverse


l = [1,2,3,4,5]
n = len(l)

# Approach1: swaping
start = 0
end = n - 1
swap = 0
while start < end:
    swap = l[start]
    l[start] = l[end]
    l[end] = swap
    start = start + 1
    end = end - 1
print(l)

# Approach2: Using insert method
l1 = [10,20,30,40,50]
l2 = []

for i in l1:
    l2.insert(0,i)

print("Second reverse list: ",l2)

# Approach3: Using slicing method
list_prime = [1,2,3,5,7]
print("The third reverse list: ",list_prime[::-1])


#Approach4: using buit- in reverse method
list_iteam = [0,9,8,7,6,5]
list_iteam.reverse()
print("Forth reverse list: ",list_iteam)