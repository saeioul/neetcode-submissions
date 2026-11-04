class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Need a map.
        aSortedWordMap = {}
        #Easiest way is group in the map identifying sorted words.
        for aWord in strs:
            aSortedWord = ''.join(sorted(aWord))
            if aSortedWord in aSortedWordMap:
                aSortedWordMap[aSortedWord].append(aWord)
            else:
                aSortedWordMap[aSortedWord] = [aWord]
        
        solutionArray = []

        for anaGroup in aSortedWordMap.values():
            solutionArray.append(anaGroup)

        return solutionArray