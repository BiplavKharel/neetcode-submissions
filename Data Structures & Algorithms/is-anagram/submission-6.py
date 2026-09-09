class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False

        s_counter = {}
        t_counter = {}

        for char in s:
            if char in s_counter:
                s_counter[char] += 1
            else:
                s_counter[char] = 1
        
        for char in t:
            if char in t_counter:
                t_counter[char] += 1
            else:
                t_counter[char] = 1
        return s_counter == t_counter