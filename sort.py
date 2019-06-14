# all sort in asc order 
# unstable methods: “快希选堆” quick/shell/select/heap

def selectionSort(arr):
    ''' 
        time complexity: O(N^2), space complexity: O(1), unstable
        
        comparing every num after the i-th number to arr[i]
        for every round (i), we select the minimum num in the unsorted array (arr[i:]) and put it at arr[i]
    '''
    for i in range(len(arr)-1):
        mini = i
        for j in range(i+1,len(arr)):
            if arr[mini] > arr[j]:
                mini = j
            arr[mini],arr[i] = arr[i],arr[mini]
    # return arr


def bubbleSort(arr):
    ''' 
        time complexity: O(N^2), space complexity: O(1), stable

        comparing adjacent nums, each time move the larger one to the right
        for every round (i), we move the (i+1)-th largest num to the position of -(i+1)
    '''
    for i in range(len(arr)-1):
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    # return arr

def bubbleSort2(arr):
    ''' 
        time complexity: O(N^2), space complexity: O(1), stable

        faster, break if no sorted happened 
    '''
    for i in range(len(arr)-1):
        isSorted = 1
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                isSorted = 0
        if isSorted: break
    # return arr


def insertionSort(arr):
    ''' 
        time complexity: O(N^2), space complexity: O(1), stable

        comparing the extracted num to the previous sorted subarray, from right to left,
        if currentSortedNum > extractedNum, move current sorted num to the right by 1
        else insert the extracted num 
        for every round (i), we move the (i+1)-th largest num to the position of -(i+1)
    '''
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            extractedNum = arr[i]
            for j in range(i-1,-1,-1):
                if arr[j] > extractedNum:
                    arr[j+1] = arr[j]
                else: break
            if j>0:
                arr[j+1] = extractedNum
            else:
                arr[j] = extractedNum
    # return arr


def mergeSort(arr):
    ''' 
        time complexity: O(NlogN), space complexity: O(N) (precisely:O(N+logN)), stable

        divide and conquer. 
        recursively divide the array into two parts and sort them,
        then combine the two sorted arrays into one array
    '''
    # base case 
    if len(arr)<2: return arr

    mid = len(arr)//2
    leftarr = mergeSort(arr[:mid])
    rightarr = mergeSort(arr[mid:])

    def merge(leftarr,rightarr):
        ''' combine the sorted left array and the sorted right array'''
        l,r = 0,0
        ret = []
        while l<len(leftarr) and r<len(rightarr):
            if leftarr[l]<rightarr[r]:
                ret.append(leftarr[l])
                l+=1
            else:
                ret.append(rightarr[r])
                r+=1

        ret+=leftarr[l:]
        ret+=rightarr[r:]
        return ret

    return merge(leftarr,rightarr)


def quickSort(arr,low,high):
    ''' 
        time complexity: O(NlogN), worst time complexity: O(N^2), space complexity: O(logN), unstable

        divide and conquer. 
        recursively partition the array, making the left part to the pivot less than it 
        and the right part to the pivot greater than it
    '''
    if low >= high: return array
    else:
        pivot = array[low]
        lo,hi=low,high
        while lo<hi:
            while lo<hi and array[hi]>=pivot:
                hi-=1
            while lo<hi and array[lo]<pivot:
                lo+=1
            if lo<hi: 
                # in this case, the pointer `hi` points to a number<pivot and 
                # pointer `lo` points to a number>=pivot, so need to exchange them
                array[lo],array[hi] = array[hi],array[lo]
        array[low],array[lo] = array[lo],array[low]
        quicksort(array,low,lo)
        quicksort(array,lo+1,high)

        return array

def quickSort2(arr):
    ''' 
        another writing method
    '''
    if len(arr)<2: return arr

    pivot = array[0]
    less = [i for i in array[1:] if i< pivot]
    greater = [i for i in array[1:] if i> pivot]
    mid = [i for i in array if i==pivot]

    return quickSort2(less) + mid + quickSort2(greater)


def heapSort(arr):
    ''' 
        time complexity: O(NlogN), space complexity: O(1), unstable

        build a max-heap of size n to size 1, max heap is a heap whose root node is at least as large as its children
        each time extract the max number and put it to the last ith position
    '''

    def maxHeapify(arr,lo,hi):
        root=lo
        while True:
            # select the left child of the root
            child=2*root+1
            # out of idx
            if child>hi: break
            # select the child with larger value
            if child+1<=hi and arr[child]<arr[child+1]: child+=1
            # exchange the child with root if it has larger value
            if arr[root]<arr[child]:
                arr[root],arr[child] = arr[child],arr[root]
                root=child
            else: break


    n=len(arr)
    # build max heap, the leaf node itself is already a max-heap
    # thus, we only need to build the max heap from the last inner node whose idx is: n//2-1
    for i in range(n//2-1,-1,-1):
        maxHeapify(arr,i,n-1)

    for i in range(n-1,0,-1):
        # extract max(arr[0]) and put it in the i-th position
        arr[i],arr[0] = arr[0],arr[i]
        maxHeapify(arr,0,i-1)

    return arr


def shellSort(arr):
    """
        time complexity: O(NlogN), worst time complexity: O(N^3), space complexity: O(1), unstable
        
        improved version of insertion sort, starting from a gap(like n//2), 
        and using insertion sort for each group of numbers (0,0+gap,0+2gap...) (1,1+gap,1+2gap...) ...
        then keep reducing the gap until it reach 1
    """
    n=len(arr)
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            if arr[i]<arr[i-gap]:
                temp=arr[i]
                j=i
                while j>=gap and arr[j-gap]>temp:
                    arr[j] = arr[j-gap]
                    j-=gap
                arr[j] = temp
        gap//=2
    return arr


def countSort(arr):
    """
        time complexity: O(N+k), space complexity: O(N+k), stable
        
        find the max,min number then define K=max-min+1, then save the occurrence of each value of i-min to cnt[i],
        then add the first j-1 counts to cnt[j], which make the cnt[i] denotes the count of numbers whose value is less than or equal to j+min 
        finally for each number i in the input arr, it locates in the idx of cnt[arr[i]-1]
    """
    n=len(arr)
    minv,maxv = min(arr),max(arr)
    K=maxv-minv+1
    cnt=[0]*K
    for i in range(n):
        cnt[arr[i]-minv]+=1
    # method 1
    idx=0
    for j in range(K):
        while cnt[j]>1:
            arr[idx]=j+minv
            idx+=1
            cnt[j]-=1

    # method 2
    # retarr=[]
    # for j in range(1,len(cnt)):
    #     cnt[j]+=cnt[j-1]
    # for j in range(n-1,-1,-1):  
    #     retarr[cnt[arr[j]] - 1] = arr[j]
    #     cnt[arr[j]]-=1
    # return retarr


def radixSort(arr,radix=10):
    """
        time complexity: O(N*M), space complexity: O(M), stable, (M is the highest digit)
        
        LSD(Least Significant Digit first) starting from the unit digit
        MSD(Most Significant Digit first) starting from the highest digit
        
        LSD: starting from the unit digit, put numbers into bucket 0-9 by their unit digit and put them back to arr
            then keep placing the numbers into buckets by higher digit, and put them back to arr
    """
    import math
    maxv=max(arr)
    hidigit = int(math.log(max(arr), radix))+1
    buckets = [[] for i in range(radix)]
    for i in range(1,hidigit+1):
        for num in arr:
            buckets[num%(radix**i) // (radix**(i-1))].append(num)
        del arr[:] # clear the arr, then arr will be empty
        for buk in buckets:
            arr.extend(buk)
        buckets = [[] for i in range(radix)]



# test
while 1:
    li = [7,5,3,8,2,7,1,4,14,23,100]
    print("\nbefore:",li)
    print("Sort methods:\n 1. Selection sort\n 2. Bubble sort\n 3. Insertion sort\n 4. Merge sort\n 5. Quick sort\n 6. Heap sort\n 7. Shell sort\n 8. Count sort\n 9. Radix sort\n")
    alg = int(input("select the sorting method: "))
    if alg==1:
        selectionSort(li)
        print("  after:",li)
    elif alg==2:
        bubbleSort2(li)
        print("  after:",li)
    elif alg==3:
        insertionSort(li)
        print("  after:",li)
    elif alg==4:
        li = mergeSort(li)
        print("  after:",li)
    elif alg==5:
        sli = quickSort(li,0,len(li)-1)
        print("  after:",li)
    elif alg==6:
        heapSort(li)
        print("  after:",li)
    elif alg==7:
        shellSort(li)
        print("  after:",li)
    elif alg==8:
        countSort(li)
        # sli = countSort(li)
        print("  after:",li)
    elif alg==9:
        radixSort(li)
        print("  after:",li)

    end = input("input anything to end, press `Enter` to continue: ")
    if end: break
