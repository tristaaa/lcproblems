class Solution(object):
    def getSum(self, a, b):
        """
            add two numbers without using +,- operations
            Bit manipulation.

            :type a: int
            :type b: int
            :rtype: int
        """
        # Since Python simulates an infinite-bit representation, not 32-bit or 64-bit
        # Ex. bin(-6) actually represented as 0b1...111111111010 
        #  (infinite string of sign bits) 计算机系统中，数值均由其补码(2's complement)表示和存储
        # Thus to simulate a 32-bit representation, we need a mask to get the last 32 bits

        # 32 bits integer max(using the first bit as sign)
        MAX = 0x7FFFFFFF
        # mask to get last 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # ^ simulate addition, but lose the info of carry  
            # & discover both 1s positions, where indicate the next position with a carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # if the summation is negative (whereas the `a` appears to be an positive number, 
        # since we just keep the last 32 bits, i.e. the first sign bit is identified as regular bit)
        
        # Eg. if a=-3 actually, we now represent it as in 32-bit form, which shows that a is 4294967293(2**32-abs(a)), which is the a's positive complement
        # and we eventually need to convert it to infinite-bit representation, we just need to add infinite 1s before our current result
        
        # Thus, we need first get `a`'s 32 bits 1's complement positive(对32位的a按位取反)
        # then get 32-bit positive's Python 1's complement negative
        return a if a <= MAX else ~(a ^ mask)


# test
a,b=-5,3
sol = Solution()
print("a= %d, b= %d, the summation of a and b= %d" % (a,b,sol.getSum(a,b)))