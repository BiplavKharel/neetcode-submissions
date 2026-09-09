class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        longest_length = 0
        l = 0

        for i in range(0,len(s)):
            
            if s[i] in seen:
                l = max(seen[s[i]] + 1,l)
            seen[s[i]] = i

            longest_length = max(longest_length,i-l+1)
        return longest_length