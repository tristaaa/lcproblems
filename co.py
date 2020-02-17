# n,m=input().split()
# n,m=int(n),int(m)
n,m=100,382
def mysum(a1,n):
    s=0
    for i in range(n):
        s+=a1
        a1=(a1+1)//2
    return s
def findA1(m,n):
    l,r=1,m
    # while l<=r:
    #     mid=(l+r)//2
    #     s=mysum(mid,n)
    #     if s==m: return mid
    #     elif s<m:l=mid+1
    #     else:r=mid-1
    # return r

    while l<r:
        mid=(l+r+1)//2
        if mysum(mid,n)>m:r=mid-1
        else:l=mid
    # if mysum(l,n)==m:return l
    # else:
    #     print("Fdsa:",l,mysum(l,n))
    return l
print(findA1(m,n))
