class Solution:

    delimiter = "#"
    def encode(self, strs: List[str]) -> str:
        resArray = []
        for aString in strs:
            resArray.append(str(len(aString)))
            resArray.append(self.delimiter)
            resArray.append(aString)
        
        print(f"Encoded {resArray}")
        return "".join(resArray)
        

    def decode(self, s: str) -> List[str]:
        decodedArray = []
        i = 0

        # For this algorith to work, AVOID ITERATORS, which are effectively immutable 
        # thus changing i won't affect the next iteration.
        while i < len(s):
            # Search for the delimiter
            j = i
            # We know there is at least one # for a non empty string.
            while s[j] != self.delimiter:
                j += 1
            # Whenever we've stopped, we are ready to extract and move on.
            stringLenSlice = int(s[i:j])
            # when indices need to be recomputed for a slice, it is clearer
            # to do it before slicing.
            i = j + 1 # We need to move our left pointer next to our delimiter.
            j = i + stringLenSlice # and move right pointer to the end fo the delimited string
            decodedArray.append(s[i:j])

            # catch up i with j's progress. 
            i = j

        return decodedArray





        return decodedArray
                    

