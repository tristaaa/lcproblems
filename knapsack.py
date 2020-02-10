#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

def f_01knapsack1(n, W):
    """
    Given a set of n items numbered from 1 up to n, 
    each with a weight wi and a value vi, 
    along with a maximum weight capacity W
    """
    # each item has its own weight and value
    w, v = [0], [0]
    dp = []
    for i in range(1, n+1):
        wi = int(input('input the weight of the '+str(i)+'th item(wi): '))
        vi = int(input('input the value of the '+str(i)+'th item(vi): '))
        w.append(wi)
        v.append(vi)

    # initialize the first row, meaning when there are zero number of item, 
    # whichever the maximum weight capacity of the bag is, the maximum value is always 0 
    dp0 = [0]*(W+1)
    dp.append(dp0)
    for i in range(1, n+1):
        dpi=[]
        for j in range(W+1):
            if j<w[i]:
                dpi.append(dp[i-1][j])
            else:
                dpi.append(max(dp[i-1][j], v[i] + dp[i-1][j-w[i]]))
        dp.append(dpi)
    return dp, w


def f_01knapsack2(n, W):
    """
    space efficient ways, using one dimension
    """
    # each item has its own weight and value
    w, v = [0], [0]
    dp = []
    for i in range(1, n+1):
        wi = int(input('input the weight of the '+str(i)+'th item(wi): '))
        vi = int(input('input the value of the '+str(i)+'th item(vi): '))
        w.append(wi)
        v.append(vi)

    # initialize the array to all 0, meaning that when using no item, 
    # the maximum value is always 0 
    dp = [0]*(W+1)

    # can write like this
    # for i in range(1, n+1):
    #     for j in range(W,0,-1):
    #         if j>= w[i]:
    #             dp[j] = max(dp[j], dp[j-w[i]] + v[i])

    # another concise way
    for i in range(1, n+1):
        for j in range(W, w[i]-1,-1):
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
    
    return dp, w

def f_bounded_knapsack1(n, W):
    """
    Given a set of n items numbered from 1 up to n, 
    each with a weight wi and a value vi, 
    and can use at most mi number of the type of the ith item,
    along with a maximum weight capacity W

    can be viewed as 0-1 knapsack problem
    """
    w, v = [0], [0]
    dp = []
    tot_cnt = 1
    for i in range(1, n+1):
        mi = int(input('input the number of the '+str(i)+'th item(mi): '))
        wi = int(input('input the weight of the '+str(i)+'th item(wi): '))
        vi = int(input('input the value of the '+str(i)+'th item(vi): '))
        w += [wi]*mi
        v += [vi]*mi
        tot_cnt += mi

    # initialize the first row, meaning when there are zero number of item, 
    # whichever the maximum weight capacity of the bag is, the maximum value is always 0 
    dp0 = [0]*(W+1)
    dp.append(dp0)
    for i in range(1, tot_cnt):
        dpi=[]
        for j in range(W+1):
            if j<w[i]:
                dpi.append(dp[i-1][j])
            else:
                dpi.append(max(dp[i-1][j], v[i] + dp[i-1][j-w[i]]))
        dp.append(dpi)

    return dp, w, tot_cnt-1


def f_bounded_knapsack2(n, W):
    """
    Given a set of n items numbered from 1 up to n, 
    each with a weight wi and a value vi, 
    and can use at most mi number of the type of the ith item,
    along with a maximum weight capacity W

    
    """
    w, v, m = [0], [0], [0]
    dp = []
    for i in range(1, n+1):
        mi = int(input('input the number of the '+str(i)+'th item(mi): '))
        wi = int(input('input the weight of the '+str(i)+'th item: '))
        vi = int(input('input the value of the '+str(i)+'th item: '))
        m.append(mi)
        w.append(wi)
        v.append(vi)

    # initialize the first row, meaning when there are zero number of item, 
    # whichever the maximum weight capacity of the bag is, the maximum value is always 0 
    dp0 = [0]*(W+1)
    dp.append(dp0)
    for i in range(1, n+1):
        dpi=[]
        for j in range(W+1):
            if j<w[i]:
                dpi.append(dp[i-1][j])
            else:
                cnt = min(m[i], j//w[i])
                dpi.append(max(dp[i-1][j], v[i] + dp[i-1][j-w[i]]))
                for k in range(2, cnt+1):
                    dpi[j] = max(dp[i-1][j], v[i]*k + dp[i-1][j-w[i]*k])
        dp.append(dpi)

    return dp, w, n


def f_unbounded_knapsack1(n, W):
    '''
    Also called complete knapscak problem, where each type of the item has unlimited number
    This is the basic version of the unbounded knapsack
    The total running time is O(nW^2) too slow
    '''
    w, v = [0], [0]
    dp = []
    for i in range(1, n+1):
        wi = int(input('input the weight of the '+str(i)+'th item(wi): '))
        vi = int(input('input the value of the '+str(i)+'th item(vi): '))
        w.append(wi)
        v.append(vi)

    # initialize the first row, meaning when there are zero number of item, 
    # whichever the maximum weight capacity of the bag is, the maximum value is always 0 
    dp0 = [0]*(W+1)
    dp.append(dp0)
    for i in range(1, n+1):
        dpi=[0]
        for j in range(1,W+1):
            dpi.append(0)
            for k in range(j//w[i]+1):
                if j>= k*w[i]:
                    dpi[j]=max(dpi[j], dp[i-1][j-k*w[i]] + k*v[i])
        dp.append(dpi)

    return dp, w, n

def f_unbounded_knapsack2(n, W):
    '''
    More efficient version of the complete knapsack problem, but still using two dimensional array
    The total running time is O(nW)
    The recurrence formula is:
        OPT(i,j) = Max(OPT(i-1,j), OPT(i,j-wi)+vi where j>=wi)
    '''
    w, v = [0], [0]
    dp = []
    for i in range(1, n+1):
        wi = int(input('input the weight of the '+str(i)+'th item(wi): '))
        vi = int(input('input the value of the '+str(i)+'th item(vi): '))
        w.append(wi)
        v.append(vi)

    # initialize the first row, meaning when there are zero number of item, 
    # whichever the maximum weight capacity of the bag is, the maximum value is always 0 
    dp0 = [0]*(W+1)
    dp.append(dp0)
    for i in range(1, n+1):
        dpi=[0]
        for j in range(1,W+1):
            dpi.append(dp[i-1][j])
            if j>= w[i]:
                dpi[j]=max(dpi[j], dpi[j-w[i]] + v[i])
        dp.append(dpi)

    return dp, w, n


def f_unbounded_knapsack3(n, W):
    '''
    More efficient version of the complete knapsack problem, and more space-efficient
    The total running time is O(nW), and the space complexity is O(n)
    The recurrence formula is:
        OPT(j) = Max(OPT(j), OPT(j-wi)+vi where j>=wi)
    '''
    w, v = [0], [0]
    dp = []
    for i in range(1, n+1):
        wi = int(input('input the weight of the '+str(i)+'th item(wi): '))
        vi = int(input('input the value of the '+str(i)+'th item(vi): '))
        w.append(wi)
        v.append(vi)

    # initialize the array to all 0, meaning that when using no item, 
    # the maximum value is always 0 
    dp = [0]*(W+1)

    # for i in range(1, n+1):
    #     for j in range(1,W+1):
    #         if j>= w[i]:
    #             dp[j]=max(dp[j], dp[j-w[i]] + v[i])
    
    for i in range(1, n+1):
            for j in range(w[i],W+1):
                dp[j]=max(dp[j], dp[j-w[i]] + v[i])

    return dp, w, n


def main(argv):
    # option: 0-1 knapsack or bounded knapsack problem(BKP) or unbounded knapsack problem(UKP)
    option = int(input('input the type of the knapsack problem(1/2/3): '))

    dp, x, w = [],[],[]
    n = int(input('input the number of items types n: '))
    W = int(input('input the maximum weight of the knapsack W: '))

    if option == 1:
        # dp,w = f_01knapsack1(n, W)
        dp,w = f_01knapsack2(n, W)
    elif option == 2:
        # dp, w, n = f_bounded_knapsack1(n, W)
        dp, w, n = f_bounded_knapsack2(n, W)
    elif option == 3:
        # dp, w = f_unbounded_knapsack1(n, W)
        # dp, w = f_unbounded_knapsack2(n, W)
        dp, w = f_unbounded_knapsack3(n, W)

    print('  '+'|\t'.join([str(j) for j in range(W+1)]))
    for i in range(n+1):
        print(str(i)+'|' + '\t'.join([str(j) for j in dp[i]]))

    print('\nmaximum value is:', dp[n][W])

    # print the specific choice of each item, xi==1 means the (i+1)-th item is choosed
    j = W
    for i in range(n, 0, -1):
        if dp[i][j]>dp[i-1][j]:
            x = [1]+x
            j -= w[i-1]
        else:
            x = [0]+x
    print('\nthe optimal solusion is choosing item: '+ ' and '.join([str(i+1) for i in range(len(x)) if x[i]==1]))


if __name__=='__main__':
    main(sys.argv)
