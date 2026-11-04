class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Count characters on sting s
        charCountMap = {}

        for character in s:
            if character in charCountMap:
                charCountMap[character] += 1
            else:
                charCountMap[character] = 1

        # Use map to substract characters.
        # not finding a character immeditely returns false.
        for character in t:
            if character in charCountMap:
                charCountMap[character] -= 1
            else:
                return False

        # Declare no anagram if any count is different to zero.
        for key, value in charCountMap.items():
            if value != 0:
                return False

        # Getting to the bottom of the programme means anagram.
        return True