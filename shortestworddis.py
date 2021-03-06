class Solution:
    def shortestDistance(self, words, word1, word2):
        """
            Given a list of words and two words word1 and word2, 
            Return the shortest distance between these two words in the list.
            
            word1 does not equal to word2, and word1 and word2 are both in the list

            :type words: List[str]
            :type word1: str
            :type word2: str
            :rtype: int
        """
        pos1,pos2=-1,-1
        shortestDis=len(words)
        for i in range(len(words)):
            if words[i] == word1:
                pos1=i
                if pos2!=-1 and pos1-pos2<shortestDis:
                    shortestDis = pos1-pos2
            elif words[i] == word2:
                pos2=i
                if pos1!=-1 and pos2-pos1<shortestDis:
                    shortestDis = pos2-pos1
        return shortestDis


sol = Solution()
words = ["practice", "makes", "perfect", "coding", "makes"]
word1,word2 = "makes","coding"
print("the shortest distance of two words: %s and %s in the list: %s is: %d" % (word1,word2,words,sol.shortestDistance(words, word1, word2)))
