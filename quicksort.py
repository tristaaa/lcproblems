def quicksort(array,low,high):
    if low < high:
        # move all the numbers smaller than pivot to the left 
        # and the numbers larger than pivot to the right
        print("\narray:%s, low:%d, high:%d\n" % (array,low,high))
        mid = partion(array,low,high)
        quicksort(array,low,mid)
        quicksort(array,mid+1,high)

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
    else: 
        pivot = array[0]
        less = [i for i in array[1:] if i< pivot]
        greater = [i for i in array[1:] if i> pivot]
        mid = [i for i in array if i==pivot]
        return quicksort2(less) + mid + quicksort2(greater)


if __name__ == '__main__':
    li = [5,3,2,1,4,6,7,0,8]
    li2 = [6,6,1,2,7,9,3,4,5,10,8]

    print("method 1")
    print("before li:",li)
    quicksort(li,0,len(li)-1)
    print("after li:",li)

    print('-'*10+"\nmethod 2")
    print("before li2:",li2)
    li2 = quicksort2(li2)
    print("after li2:",li2)
