n,m=input().split()
n,m=int(n),int(m)

def mysum(a1,n):
    s=0
    for i in range(n):
        s+=a1
        a1=(a1+1)//2
    return s
def findA1(m,n):
    l,r=1,m
    while l<=r:
        mid=(l+r)//2
        s=mysum(mid,n)
        if s==m: return mid
        elif s<m:l+=1
        else:r-=1

    return r
print(findA1(m,n))
