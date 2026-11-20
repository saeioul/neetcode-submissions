class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Just leverage the sorting
        sortedKeyMap = {}
        responseList = []

        #Collect the words that match when ordered.
        for aWord in strs:
            sortedKey = "".join(sorted(aWord))

            if sortedKey in sortedKeyMap:
                sortedKeyMap[sortedKey].append(aWord)
            else:
                sortedKeyMap[sortedKey] = [aWord]

        for groupedWords in sortedKeyMap.values():
            responseList.append(groupedWords)

        return responseList