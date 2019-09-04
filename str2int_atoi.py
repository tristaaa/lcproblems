class Solution:
    def myAtoi(self, s):
        """
            Implement `atoi` which converts a string to an integer.

            The function first discards as many whitespace characters as necessary 
            until the first non-whitespace character is found.
            Then, starting from this character, takes an optional initial plus or minus sign
            followed by as many numerical digits as possible, 
            and interprets them as a numerical value.

            String can contain additional characters after those that form the integral number, 
            which are ignored and have no effect on the behavior of this function.

            If the first sequence of non-whitespace characters in str is not a valid integral number, 
            or if no such sequence exists because either str is empty or it contains only whitespace characters, 
            no conversion is performed.
            If no valid conversion could be performed, a zero value is returned.

            Note:
                Only the space character ' ' is considered as whitespace character.
                Assume we are dealing with an environment which could only store integers 
                within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
                If the numerical value is out of the range of representable values, 
                INT_MAX (2^31 − 1)=2147483647 or INT_MIN (−2^31) is returned.
            

            :type str: str
            :rtype: int
        """
        sign=0
        i=0
        result=0
        INT_MAX=2**31-1
        while(s[i]==' '):
            i+=1
        if s[i] in ['+','-']:
            sign = 1-(s[i]=='-')*2
            i+=1
        while (i<len(s) and s[i] in '0123456789'):
            if result>INT_MAX//10 or result==INT_MAX//10 and ord(s[i])-ord('0')>7:
                return INT_MAX if sign==1 else sign*(INT_MAX+1)
            result = result*10 + ord(s[i])-ord('0')
            i+=1
        return sign*result


sol = Solution()
s = "   -42 with words"
s1 = "   abc-42 with words"
s2 = "   -2147483649"
s3 = "   +- 3"
s4 = "   -"
print("my atoi function to convert a string to integer")
print("will return 0 if string only contain whitespace chars, or the first char which is non-whitespace isn't a valid number")
print("will return INT_MAX (2^31 − 1) or INT_MIN (−2^31) if the converted number is out of range(32-bit int)")
print("for string '%s', the return value is: %d" % (s,sol.myAtoi(s)))
print("for string '%s', the return value is: %d" % (s1,sol.myAtoi(s1)))
print("for string '%s', the return value is: %d" % (s2,sol.myAtoi(s2)))
print("for string '%s', the return value is: %d" % (s3,sol.myAtoi(s3)))
print("for string '%s', the return value is: %d" % (s4,sol.myAtoi(s4)))


