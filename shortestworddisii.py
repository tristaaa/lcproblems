class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.n = len(words)
        self.word2idx = {}
        for i in range(self.n):
            if words[i] not in self.word2idx:
                self.word2idx[words[i]] = [i]
            else:
                self.word2idx[words[i]] += [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # method 1, O(M*N) where M=len(word2idx[word1]) and N=len(word2idx[word2])
        shortestDis = self.n
        for i in self.word2idx[word1]:
            for j in self.word2idx[word2]:
                if abs(i-j)<shortestDis:
                    shortestDis = abs(i-j)

        return shortestDis

        # method 2, O(M+N) where M=len(word2idx[word1]) and N=len(word2idx[word2])
        # using two pointers, the pointer only moves on when it points to the lower index
        shortestDis = self.n
        pos1,pos2 = 0,0
        l1,l2 = self.word2idx[word1],word2idx[word2]
        while pos1<len(l1) and pos2<len(l2):
            if abs(l1[pos1]-l2[pos2])<shortestDis:
                shortestDis = abs(l1[pos1]-l2[pos2])
            if l1[pos1]<l2[pos2]:
                pos1+=1
            else:
                pos2+=1

        return shortestDis

words = ["practice", "makes", "perfect", "coding", "makes"]
wordDistance = WordDistance(words)

# call function
word1,word2 = "makes","coding"
shortestDis = wordDistance.shortest(word1,word2)
print("the shortest distance of two words: %s and %s in the list: %s is: %d" % (word1,word2,words,shortestDis))

# call function again
word1,word2 = "practice","coding"
shortestDis = wordDistance.shortest(word1,word2)
print("the shortest distance of two words: %s and %s in the list: %s is: %d" % (word1,word2,words,shortestDis))
