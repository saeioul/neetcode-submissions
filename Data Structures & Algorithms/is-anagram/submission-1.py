class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        # Count words in the first array.
        for i in range(0, len(s)):
            value = s[i]
            if value in seen:
                seen[value] = seen[value] + 1
            else:
                seen[value] = 1
        # Remove words. A valid anagram will have all keys == 0
        sum = 0
        for i in range(0, len(t)):
            value = t[i]
            if value in seen:
                if seen[value] == 0:
                    return False
                else:
                    seen[value] = seen[value] -1 
            else:
                return False
        
        for remainingCount in seen.values():
            if remainingCount != 0:
                return False



        return True
            
