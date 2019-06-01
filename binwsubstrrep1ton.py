class Solution:
    def queryString(self, S, N):
        """
            return true if and only if for every integer X from 1 to N, 
            the binary representation of X is a substring of S.
            Note: len(S)<=1000
            
            :type S: str
            :type N: int
            :rtype: bool
        """
        # basic version [32 ms]
        for x in range(N,0,-1):
            if bin(x)[2:] not in S: return False
        return True

        # improved
        # 1) for every i < N/2, the binary string of 2*i will contain binary string of i
        #    Eg. bin(5) is '0b101' and bin(10) is '0b1010', bin(2i) is just bin(i)+'0'
        #    so we only need to check half of the numbers less than N
        # 2) We know that for any string of length LS, we can at most have `LS - 9` different binary digits of length 10
        #    So, given that len(S)=1000, we know that it can caontain at most 991 different numbers whose binary digits are of length 10
        #    We know that the number 1000-1999 have 1000 different binary digits of length 10
        #    Thus, given the condition, the given N cannot be larger than 2000(preceisely <1991)
        if N > len(S) * 2: return False
        return all(bin(i)[2:] in S for i in range(N, N//2, -1))


# test
sol=Solution()
S="1011100"
N=7
print("for every integer number 1<=X<=N (N= %d), the binary representation of X is a substring of S (S= '%s'): %s" % (N,S,sol.queryString(S,N)))