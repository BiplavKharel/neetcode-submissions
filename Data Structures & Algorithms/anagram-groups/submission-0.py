class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        group_dict = defaultdict(list)
        for word in strs:
            hashes = [0] * 26
            for char in word:
                hashes[ord(char) - ord('a')] += 1
            group_dict[tuple(hashes)].append(word)
        return group_dict.values()
            