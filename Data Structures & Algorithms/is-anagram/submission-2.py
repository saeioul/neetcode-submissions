class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        for i in range(0,len(s)):
            character = s[i]
            if character in charMap:
                charMap[character] = charMap[character] + 1
            else:
                charMap[character] = 1
        
        for i in range(0, len(t)):
            character = t[i]
            if character in charMap:
                if charMap[character] < 1:
                    return False
                charMap[character] = charMap[character] - 1
            else:
                return False
            
        
        for value in charMap.values():
            if value != 0:
                return False


        return True
        