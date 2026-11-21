class Solution:

    # Chosen delimiter. We will know its always after the encoded length.
    delim = "#"
    '''
    Easiest solution is to encode every string length.
    This let us know how many characters we expect in advance,
    avoiding having to do special char escape gymnastics
    '''
    def encode(self, strs: List[str]) -> str:
        # An array is a good holder
        strList = []
        for aWord in strs:
            strList.append(str(len(aWord)))
            strList.append(self.delim)
            strList.append(aWord)

        return "".join(strList)

    def decode(self, s: str) -> List[str]:
        # Representation first:
        # s = [ N,# ,string, ... , N , #, string]

        #print(f"Input: {s}")
        response = []
        # Main pointer drives decoding:
        i = 0
        while i < len(s):
            # Second pointer chases delimiter. Assumes representation 
            j = i
            while s[j] != self.delim:
                j += 1

            sizeToDecode = int(s[i:j])
            #print(f"size to decode: {sizeToDecode}")
            # update decoder driver 
            i = j + 1
            j = j + sizeToDecode + 1 

            # Cut between delimiter last known position and size to decode.
            decodedString = s[i:j]
            #print(f"decoded string: {decodedString}")

            # Update i for next loop
            i = j

            response.append(decodedString)

        return response



