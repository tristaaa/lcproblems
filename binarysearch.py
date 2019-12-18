def binary_search(a, T):
    l,r=0,len(a)-1
    while l<=r:
        m=(l+r)//2 # floor
        print("l,m,r:",l,m,r)
        if a[m]<T: l=m+1
        elif a[m]>T: r=m-1
        else: return m

    return -1 # unseccessful

def binary_search_alter(a, T):
    l,r=0,len(a)-1
    while l<r:
        m=(l+r+1)//2 # ceil
        print("l,m,r:",l,m,r)
        if a[m]>T: r=m-1
        else: l=m

    if a[l]==T: return l
    return -1 # unseccessful

def binary_search_leftmost(a, T):
    l,r=0,len(a)
    while l<r:
        m=(l+r+1)//2 # floor
        print("l,m,r:",l,m,r)
        if a[m]<T: l=m+1
        else: r=m

    return l

def binary_search_rightmost(a, T):
    l,r=0,len(a)
    while l<r:
        m=(l+r)//2 # floor
        print("l,m,r:",l,m,r)
        if a[m]>T: r=m
        else: l=m+1

    return l-1


a=[1,2,4,4,4,5,6,7]
T=4 # target

print()
print("input array: %s, target: %d"%(a,T))
print("1. Basic Binary Search, with checking whether the a[m]==T in every loop")
print("the index of the target number is: ",binary_search(a,T))

print()
print("2. Alternative Binary Search, leaving out checking whether the a[m]==T in every loop,"+
    "faster comparison but require one more iteration on average.")
print("the index of the target number is: ",binary_search_alter(a,T))

print()
print("3. Leftmost Binary Search, when there are duplicate targets, always find the leftmost target")
print("Even if the target is not in the array, L is the number of elements in the array that are less than T")
print("the index of the target number is: ",binary_search_leftmost(a,T))

print()
print("4. Rightmost Binary Search, when there are duplicate targets, always find the rightmost target")
print("Even if the target is not in the array, n-L is the number of elements in the array that are greater than T")
print("the index of the target number is: ",binary_search_rightmost(a,T))

