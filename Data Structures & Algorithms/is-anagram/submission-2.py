class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for i in s:
        #     if i not in t:
        #         return False
        # return True

        if len(s) != len(t):
            return False

        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) +1
            countT[t[i]] = countT.get(t[i],0) +1

        return countS == countT
