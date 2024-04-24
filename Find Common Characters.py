class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        
        char_count = Counter(words[0])

        for word in words[1:]:
            word_count = Counter(word)
            for char in char_count:
                char_count[char] = min(char_count[char], word_count[char])

        result = []
        for char, count in char_count.items():
            result.extend([char] * count)

        return result
