# 小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，现在小Q想用这些歌组成一个总长度正好为K的歌单，
# 每首歌最多只能在歌单中出现一次，在不考虑歌单内歌曲的先后顺序的情况下，请问有多少种组成歌单的方法。

def countSongComb(k,a,x,b,y):
    """
    since the result can be very large, must mod the result with 1000000007
    
    :type k: int, length of song list 1<=k<=1000
    :type a: int, length of type1 song, 1<=a<=10
    :type x: int, number of type1 songs, 1<=x<=100
    :type b: int, length of type2 song, 1<=b<=10, b≠a
    :type y: int, number of type2 songs, 1<=y<=100
    :rtype: int
    """
    # initial dp
    # like 01 knapsack
    # dp[i][j] means the number of different combination of the song list with length j given i songs
    dp=[[0]*(k+1) for i in range(x+y+1)]

    w=[0] # the "weight"(length) for each song

    # initilize
    for i in range(x+y+1):
        dp[i][0]=1 # if the song list is of length zero, there will always be one way to make up the song list
    for i in range(x): # there are x songs with length a
        w.append(a)
    for i in range(y): # there are y songs with length b
        w.append(b)

    MOD=1000000007
    for i in range(1,x+y+1):
        for j in range(k+1):
            if j>=w[i]:
                dp[i][j]=(dp[i-1][j]+dp[i-1][j-w[i]])%MOD
            else:
                dp[i][j]=dp[i-1][j]

    return dp[x+y][k]%MOD



    # space efficient dp
    # like 01 knapsack
    # dp[i] means the number of different combination of the song list with length i
    dp=[0]*(k+1)

    # initilize
    dp[0]=1 # if the song list is of length zero, there will always be one way to make up the song list

    MOD=1000000007
    for i in range(x):
        for j in range(k,a-1,-1):
            dp[j]=(dp[j]+dp[j-a])%MOD

    for i in range(y):
        for j in range(k,b-1,-1):
            dp[j]=(dp[j]+dp[j-b])%MOD

    return dp[k]%MOD




# input will be like (first row:k; second row: a x b y):
# 5
# 2 3 3 3
k=int(input("please input the length of the song list, k="))
a,x,b,y=list(map(int,input("please input the length of type1 song, number of type1 song, length of type2 song, number of type2 song(split with space): a,x,b,y=").split()))
print("\nThe number of different combination of the song list with length k=%d, given x=%d songs with length a=%d and y=%d songs with length b=%d will be: %d" % (k,x,a,y,b,countSongComb(k, a, x, b, y)))
