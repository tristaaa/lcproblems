class Solution:
    def findSubstring(self, s, words):
        """
            find all starting idx of substr in given string that 
            is a concatenation of all words in given list, no repeating word, no other chars

            :type s: str
            :type words: List[str]
            :rtype: List[int]
        """
        # method 1 [60 ms]
        # consider s as several series of words with length k starting at [0, k-1]. 
        # For example "barfoothe" with  k= 3, 
        # can be view as ["bar", "foo", "the"] for i=0 
        # and ["arf", "oot"] for i = 1 
        # and ["rfo", "oth"] for i = 2
        if not s or not words: return []

        n=len(s)
        wordlen = len(words[0])
        substrlen = len(words)*wordlen

        freq = {}
        for w in words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w]=1

        ret=[]

        def findIdx(low):
            high=low
            curr={}
            while high+wordlen<=n:
                word = s[high:high+wordlen]
                high+=wordlen
                if word in freq:
                    curr[word] = curr[word]+1 if word in curr else 1
                    while curr[word] > freq[word]:
                        curr[s[low:low+wordlen]] -=1
                        low+=wordlen
                    if high-low==substrlen:
                        ret.append(low)
                else:
                    low=high
                    curr.clear()


        for i in range(min(wordlen,n-substrlen+1)):
            findIdx(i)

        return ret




# test
sol=Solution()
s="barfoothefoobarman"
words = ["foo","bar"]
print("all starting idx of substr in string s: '%s' that is a concatenation of all words in %s (no repeating word, no other chars) is: %s" % (s,words,sol.findSubstring(s,words)))