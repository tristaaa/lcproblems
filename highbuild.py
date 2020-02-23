# 小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。
# 小Q从第一栋一直走到了最后一栋，所以他想知道他在每栋楼的位置处能看到多少栋楼呢？
# （当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住） 

def highBuilding(n,arr):
    stack=[]
    lookleft,lookright=[0]*n,[0]*n
    for i in range(n):
        lookleft[i]=len(stack)
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        stack.append(arr[i])

    stack=[]
    for i in range(n-1,-1,-1):
        lookright[i]=len(stack)
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        stack.append(arr[i])

    return [1+lookleft[i]+lookright[i] for i in range(n)]

n=int(input())
arr=list(map(int,input().split()))
print("the number of building can be seen from the ith building are(incliding itself):",highBuilding(n,arr))
