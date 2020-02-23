# 作为程序员的小Q，他的数列和其他人的不太一样，他有个数。
# 老板问了小Q一共 m次，每次给出一个整数, 要求小Q把这些数每分为一组，然后把每组进行翻转，小Q想知道每次操作后整个序列中的逆序对个数是多少呢？

# 例如:
# 对于序列1 3 4 2，逆序对有(4, 2),(3, 2),总数量为2。
# 翻转之后为2 4 3 1，逆序对有(2, 1),(4, 3), (4, 1), (3, 1),总数量为4。

def inversionpair(n,arr,m,qarr):
    """
    :type n: int, 0<=n<=20
    :type arr: List[int], the initial sequence, of length 2^n, 0<=n<=20
    :type m: int, length of qarr, 1<=m<=10^6
    :type qarr: List[int], list of qi, qi indicates the size of group to be inversed, 0<=qi<=n
    :rtype: List[int], return list of inversion pairs regarding each qi
    """
    count=0
    for qi in qarr:
        count=0
        arr=dorever(arr,2**n,qi)
        print(count)


def dorever(arr,n,qi):
    lo=0
    for i in range(n//2**qi):
        l,r=lo,lo+2**qi-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        lo+=2**qi
        
    arr_cp=arr[:]
    mergeSort(arr,0,n)
    return arr_cp

def mergeSort(arr,low,high):
    if low<high:
        mid =(low+high)//2;
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    ret =[]
    i=low
    j=mid+1
    while i<=mid and j<=high:
        if arr[i]<=arr[j]:
            ret.append(arr[i])
            i+=1
        else:
            count+=mid-i+1
            count%=1000000007
            ret.append(arr[j])
            j+=1
        
    
    while i<=mid:
        ret.append(arr[i])
    while j<=high:
        ret.append(arr[j])
    for i in range(len(ret)):
        arr[i+low]=ret[i]
   


n=2
arr=[2,1,4,3]
m=4
qarr=[1,2,0,2]
print(inversionpair(n,arr,m,qarr))
