class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCharMap = {}
        tCharMap = {}
        for i in range(0,len(s)):
            if s[i] not in sCharMap:
                sCharMap[s[i]] = 1
            else:
                sCharMap[s[i]] += 1
            if t[i] not in tCharMap:
                tCharMap[t[i]] = 1
            else:
                tCharMap[t[i]] += 1   
        return sCharMap == tCharMap       