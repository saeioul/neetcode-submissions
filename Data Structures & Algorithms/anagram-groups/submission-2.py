class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Easiest strategy is create a map with sorted strings
        so we can identify every anagram as a group.
        '''

        anaMap = {}
        response = []

        for aString in strs:
            aSortedStr = "".join(sorted(aString))
            if aSortedStr in anaMap:
                anaMap[aSortedStr].append(aString)
            else:
                anaMap[aSortedStr] = [aString]
            
        
        for aGroup in anaMap.values():
            response.append(aGroup)

        return response