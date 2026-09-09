from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)


        for word in strs:
            freq = [0] * 26 
            for char in word:
                freq[ord(char) - ord('a')] += 1
            # How can you turn this frequency mapping into a key
            # Python can hash tuples
            res[tuple(freq)].append(word)
        return list(res.values())



