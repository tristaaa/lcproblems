class Solution:
    def multiply(self, num1, num2):
        """
            multiply two numbers in string form, and return the result as string.
            Cannot use int() to directly convert the string to integer.
            :type num1: str
            :type num2: str
            :rtype: str
        """
        # method 1
        product = [0]*(len(num1)+len(num2))
        pos=len(product)-1

        for i in num1[::-1]:
            innerpos = pos
            for j in num2[::-1]:
                product[innerpos]+=(ord(i)-ord('0'))*(ord(j)-ord('0'))
                product[innerpos-1]+=product[innerpos]//10
                product[innerpos]%=10
                innerpos-=1
            pos-=1
        
        st=0
        while product[st]==0 and st<len(product)-1:
            st+=1
        return ''.join(map(str,product[st:]))

        # method 2
        # notice that for two string representing numbers, 
        # the idx i digit of num1 and the idx j digit of num2 will contribute to 
        # the idx (i+j) digit of result and idx (i+j+1) digit of result 
        # product = [0]*(len(num1)+len(num2))

        # for i in range(len(num1)-1,-1,-1):
        #     for j in range(len(num2)-1,-1,-1):
        #         pos = i+j+1
        #         carry,num = divmod((ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))+product[pos],10)
        #         product[pos]=num
        #         product[pos-1]+=carry
        
        # st=0
        # while product[st]==0 and st<len(product)-1:
        #     st+=1
        # return ''.join(map(str,product[st:]))



# test
sol = Solution()
num1,num2="123","456"
print("num1= %s, num2= %s, the product of num1 and num2= %s" % (num1,num2,sol.multiply(num1,num2))) #56088