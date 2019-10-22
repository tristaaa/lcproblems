class Solution:
    def beforAndAfterPuzzles(self, phrases):
        """
            Before and After puzzles are phrases that are formed by merging two phrases 
            where the last word of the first phrase is the same as the first word of the second phrase
            Return the Before and After puzzles that can be formed by every two phrases 
            phrases[i] and phrases[j] where i != j. Consider both orders of any two phrases

            Return a list of distinct strings sorted lexicographically
            
            :type phrases: List[str]
            :rtype: List[str]
        """
        # ret=[]
        # # a dict to store the head and tail word of each phrase
        # joinword = {}
        # for i in range(len(phrases)):
        #     words = phrases[i].split()
        #     joinword[i] = (words[0],words[-1])

        # for i in range(len(phrases)):
        #     for k,v in joinword.items():
        #         if k!=i and v[0]==joinword[i][1]:
        #             ret.append(phrases[i] + phrases[k][len(v[0]):])

        # return sorted(set(ret))

        P, F, A = [], {}, set()
        for i in phrases: P.append(i.split())

        for i,j in enumerate(P):
            a = j[0]
            if a in F: F[a].append(i)
            else: F[a] = [i]

        print(P)

        for i,j in enumerate(P):
            b = j[-1]
            if b not in F: continue
            for k in F[b]:
                if i == k: continue
                A.add(" ".join(j + P[k][1:]))
        return sorted(A)


sol = Solution()
phrases =  ["mission statement",
                  "a quick bite to eat",
                  "a chip off the old block",
                  "chocolate bar",
                  "mission impossible",
                  "a man on a mission",
                  "block party",
                  "eat my words",
                  "bar of soap"]
print("the before and after puzzles of the phrases list:\n %s are:\n %s" % (phrases, sol.beforAndAfterPuzzles(phrases)))

