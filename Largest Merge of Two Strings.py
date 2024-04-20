class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        new = []
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                new.append(word1[i])
                i += 1
            elif word1[i] < word2[j]:
                new.append(word2[j])
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    new.append(word1[i])
                    i += 1
                else:
                    new.append(word2[j])
                    j += 1
        
        new.extend(word1[i:])
        new.extend(word2[j:])
        
        return ''.join(new)
