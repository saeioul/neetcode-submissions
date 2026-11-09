class Solution:

    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        anArray = []
        for aStr in strs:
            anArray.append(str(len(aStr)))
            anArray.append(self.delimiter)
            anArray.append(aStr)
        return "".join(anArray)

    def decode(self, s: str) -> List[str]:
        response = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != self.delimiter:
                j += 1
            lenToDecode = int(s[i:j])
            # Update i so it is right after delimiter
            i = j + 1
            # Update j so it is right after the decoded size
            j = i + lenToDecode
            # Exctract our decoded string
            decodedStr = s[i:j]
            response.append(decodedStr)
            # Update i so we can finish eventually
            i = j

        return response


