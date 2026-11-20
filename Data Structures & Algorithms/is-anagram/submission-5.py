class Solution:
    # Ona approach is counting chars.
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}

        for character in s:
            if character in charMap:
                charMap[character] += 1
            else:
                charMap[character] = 1

        for character in t:
            if character in charMap:
                charMap[character] -= 1
            else:
                return False
        
        for key, value in charMap.items():
            if value != 0:
                return False

        return True
