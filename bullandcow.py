class Solution:
    def getHint(self, secret, guess):
        """
        return the hint showing how many bulls and cows are in the guess.
            bulls are digits in guess that match the secret both in number and position
            cows are digits in guess that only match the secret in number, not location
        return example: '2A1B' meaning 2 bulls and 1 cow
        both input string only contain digits and are of same length
        duplicate digits in guess as cow for one specific digit in secret only count once

        :type secret: str
        :type guess: str
        :rtype: str
        """
        # [48 ms]
        bulls,cows=0,0
        seendigit=collections.defaultdict(int)

        for i in range(len(secret)):
            if guess[i]==secret[i]:
                bulls+=1
            else:
                if seendigit[secret[i]]<0:
                    cows+=1
                if seendigit[guess[i]]>0:
                    cows+=1
                # seendigit store the number of times that a digit appears in the secert and guess
                # when it is negative, it means it appears in guess more than in secret in first i+1 elements
                seendigit[secret[i]]+=1
                seendigit[guess[i]]-=1

        return str(bulls)+'A'+str(cows)+'B'



sol=Solution()
li = [("1807","7810"),("1123","0111"),("1100","0011"),("1122","1222")]
print("Now playing the bulls and cows game, follwing function will show the hints, xAyB means there are x bulls and y cows.")
print("Bulls are digits in guess that match the secret both in number and position\n Cows are digits in guess that only match the secret in number, not location")
for secret,guess in li:
    # result should be 1A3B 1A1B 0A4B 3A0B
    print("Given the secret str=%s and guess str=%s, the hints are: %s" % (secret, guess, sol.getHint(secret,guess)))