class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Easiest and more robust is leveraging sorting.
        theMapOfStrings = {}
        for i in range(0, len(strs)):
            sortedString = ''.join(sorted(strs[i]))
            if sortedString in theMapOfStrings:
                theMapOfStrings[sortedString].append(strs[i])
            else:
                theMapOfStrings[sortedString] = [strs[i]]
        return list(theMapOfStrings.values())


