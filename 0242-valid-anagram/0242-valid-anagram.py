class Solution(object):
    # def isAnagram(self, s, t):
    #     if len(s)!=len(t):
    #         return False
    #     countS, countT = {}, {}

    #     for i in range(len(s)):
    #         # if not in the dictionary, return with 0
    #         countS[s[i]] = 1 + countS.get(s[i],0)
    #         countT[t[i]] = 1 + countT.get(t[i],0)
        
    #     return countS ==  countT

    def isAnagram(self,s,t):
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False


        """
        :type s: str
        :type t: str
        :rtype: bool
        """