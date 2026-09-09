class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        l = 0
        longest_seen = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            longest_seen = max(len(seen),longest_seen)
        return longest_seen

