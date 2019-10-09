class Solution:
    def countCharacters(self, words, chars):
        """
        You are given an array of strings words and a string chars.
        A string is good if it can be formed by characters from chars 
        (each character can only be used once for one word).
        Return the sum of lengths of all good strings in words.
        
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        # [96 ms]
        length=0
        chardict = {}
        for c in chars:
            if c in chardict:
                chardict[c]+=1
            else:
                chardict[c]=1

        for word in words:
            flag=True
            for l in word:
                if l not in chardict or chardict[l]<word.count(l):
                    flag=False
                    break
            if flag:
                length+=len(word)
        return length
                
sol = Solution()
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
# The strings that can be formed are "hello" and "world" 
# so the answer is 5 + 5 = 10
print("the length of words (each word is from the words list: %s) that can be formed from the characters in '%s' is: %d " % (words, chars, sol.countCharacters(words,chars)))
