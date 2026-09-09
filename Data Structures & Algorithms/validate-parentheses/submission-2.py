class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        counter_parts = {']':'[','}':'{',')':'('}
        for char in s:
            if char in counter_parts.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if counter_parts[char] != stack[-1]:
                    return False
                stack.pop(-1)
        return len(stack) == 0

                