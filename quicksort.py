# def quicksort(array,low,high):
#     if low < high:
#         # # move all the numbers smaller than pivot to the left 
#         # # and the numbers larger than pivot to the right
#         # print("\narray:%s, low:%d, high:%d\n" % (array,low,high))
#         # mid = partion(array,low,high)
#         # quicksort(array,low,mid)
#         # quicksort(array,mid+1,high)
#         pivot = array[low]
#         lo,hi=low,high
#         while lo<hi:
#             while lo<hi and array[hi]>=pivot:
#                 hi-=1
#             while lo<hi and array[lo]<pivot:
#                 lo+=1
#             if lo<hi:
#                 array[lo],array[hi] = array[hi],array[lo]
#         array[low],array[lo] = array[lo],array[low]
#         quicksort(array,low,lo)
#         quicksort(array,lo+1,high)
#         return array
#     else: return array

def partion(array,low,high):
    pivot = array[low]
    while low < high:
        while low < high and array[high] >= pivot:
            high -= 1
        if low < high: # find a number smaller than the pivot
            array[low] = array[high]
            # print("move smaller val(%d) to the left position(%d):" % (array[high], low))
            # print("  array:%s"%(array))

        while low < high and array[low] < pivot:
            low += 1
        if low < high:
            array[high] = array[low]
            # print("move higher val(%d) to the right position(%d):" % (array[low], high))
            # print("  array:%s"%(array))

    array[low] = pivot
    return low


def quicksort2(array):
    if len(array)<2: return array
    pivot = array[0]
    less = [i for i in array[1:] if i< pivot]
    greater = [i for i in array[1:] if i> pivot]
    mid = [i for i in array if i==pivot]
    return quicksort2(less) + mid + quicksort2(greater)


def heap_sort(ary) :
    n = len(ary)
    for start in range(n//2-1,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary


def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break

if __name__ == '__main__':
    li = [5,3,2,1,4,6,7,0,8]
    li2 = [6,6,1,2,7,9,3,4,5,10,8]

    ll=heap_sort(li)
    print(ll,li)
    # print("method 1")
    # print("before li:",li)
    # li=quicksort(li,0,len(li)-1)
    # print("after li:",li)

    # print('-'*10+"\nmethod 2")
    # print("before li2:",li2)
    # li2 = quicksort2(li2)
    # print("after li2:",li2)
