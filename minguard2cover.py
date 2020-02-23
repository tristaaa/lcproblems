# 小Q在进行一场竞技游戏,这场游戏的胜负关键就在于能否能争夺一条长度为L的河道,即可以看作是[0,L]的一条数轴。
# 这款竞技游戏当中有n个可以提供视野的道具−真视守卫,第i个真视守卫能够覆盖区间[xi,yi]。
# 现在小Q想知道至少用几个真视守卫就可以覆盖整段河道。 (无解则返回-1)
# 输入包括n+1行。
# 第一行包括两个正整数n和L(1<=n<=105,1<=L<=109)
# 接下来的n行,每行两个正整数xi,yi(0<=xi<=yi<=109),表示第i个真视守卫覆盖的区间。 

# n,l=map(int,input().split())
# guard=[]
# for i in range(n):
#     guard.append(tuple(map(int,input().split())))
n,l=4,6
guard=[(3,6),(2,4),(0,2),(4,7)]
    
# sort first by left bound asc, then by right bound desc
guard.sort(key=lambda x: (x[0],-x[1]))
minguard=0
# lf,ri indicate the left and right bound of the current cover area
# finally, we want lf<=0 and ri>=l
i,lf,ri=0,0,0
# greedy, find guards whose left bound are left to the current cover area and choose one that can reach the rightmost position
while i<n:
    # for guards whose left bound is less than or equal to the lf
    while i<n and guard[i][0]<=lf:
        ri=max(ri,guard[i][1])
        i+=1
    minguard+=1
    lf=ri
    # we cannot find a guard whose left bound is left to the current cover area, so no answer
    if i<n and guard[i][0]>lf:
        minguard=-1
        break
    # early break, when the curret cover area is right to the l, we can stop and return the answer
    if ri>=l:break
   
# when in the end the current cover area cannot extend right to the l, no answer
if ri<l: print(-1)
else: print(minguard)
