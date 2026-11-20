class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorting can do things for you
        if sorted(s) == sorted(t):
            return True
        
        return False