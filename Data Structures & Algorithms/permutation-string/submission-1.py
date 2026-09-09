
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        counter = [0] * 26
        s1_map = [0] * 26
        for char in s1:
            s1_map[ord(char) - ord('a')] += 1

        for r in range(len(s2)):
            counter[ord(s2[r]) - ord('a')] += 1
            
            if (r - l + 1) > len(s1):
                counter[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if s1_map == counter and r - l + 1 == len(s1):
                return True
                
        return False
