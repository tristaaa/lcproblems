import collections

class Solution:
    def findSubstringInWraproundString(self, p):
        """
            count unique substring(s) of `p` which exists in string `s`.
            string `s` is an infinite warparound string of alphabatic lowercase letters.

            :type p: str
            :rtype: int
        """

        # method 1 [72 ms]
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            # if we know the max number of unique substrings in p ends with 'a','b'...'z', 
            # then the summary of them is the answer.
            # 1) The max number of unique substring ends with a letter equals to 
            #    the length of max contiguous substring ends with that letter.
            # 2) If there are overlapping, we only need to consider the longest one 
            #    because it covers all the possible unique substrings.
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())

        # improved version, little bit faster [68 ms]
        res = {i: 1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) in [1,-25] else 1
            if l>res[j]: res[j]=l
        return sum(res.values())

        # method 2 [68 ms]
        if len(p) <= 1:
            return len(p)
        count = collections.defaultdict(int)
        max_length = 1
        count[p[0]] = 1
        match = "zabcdefghijklmnopqrstuvwxyz"
        for i in range(1, len(p)):
            if p[i-1] + p[i] in match:
                max_length += 1
            else:
                max_length = 1
            # count[p[i]] = max(count[p[i]], max_length)
            if max_length>count[p[i]]:
                count[p[i]]=max_length
        return sum(count.values())


# test
sol=Solution()
p="zabc"
print("the number of unique substrings of string p: '%s' that are present in string s(an infinite wraparound string of 'abcd...z') is: %d" % (p,sol.findSubstringInWraproundString(p)))