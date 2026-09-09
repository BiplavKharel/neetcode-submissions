from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq_map = {}
        max_length = 0
        l = 0
        for i in range(len(s)):
            freq_map[s[i]] = 1 + freq_map.get(s[i],0)
            while (i - l + 1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1
            max_length = max(max_length,i-l+1)
        return max_length
