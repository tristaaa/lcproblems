class Solution:
    def primePalindrome(self, N):
        """
            Find the smallest prime palindrome >= N.
            1<=N<=10**8

            :type N: int
            :rtype: int
        """
        # there is a trick: a palindrome with even length of digits cannot be a prime
        # since they can all be divisible by 11 except for 11 itself.
        # Eg. a palindrome 123321=1*100000+2*10000+3*1000+3*100+2*10+1,
        # since 10%11=10 or -1, 100%11=1, 1000%11=10 or -1, 10000%11=1, 100000%11=10 or -1
        # and 123321 % 11 = 1*(-1)+2*1+3*(-1)+3*1+2*(-1)+1*1=0, the symmetric digits cancel out.

        # method 1 [72 ms]
        def isPrime(x):
            if x%2==0: return False
            # if x%2==0 or x<2: return x==2
            for i in range(3,int(x**0.5)+1,2):
                if x%i==0: return False
            return True

        if N<=11: 
            for i in [2,3,5,7,11]:
                if i>=N: return i
                
        i=10**(len(str(N))//2)
        while i<10**5:
        # for i in range(10**(len(str(N))//2),10**5):
            stri = str(i)
            # if the number i start with an even digit, the palindrome it formed cannot be a prime
            if int(stri[0])%2==0: 
                i=i+10**(len(stri)//2)
                continue
            y=int(stri+stri[-2::-1])
            if y>=N and isPrime(y): return y
            i+=1

# test
sol=Solution()
Ns=[1,2,3,4,5,6,7,8,9,13,143,1222,4575]
for N in Ns:
    print("N= %d, the smallest prime palindrome >= N is: %d" %(N,sol.primePalindrome(N)))
    