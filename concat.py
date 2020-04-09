class Solution:
    def findAllConcatenatedWords(self, words):
        wordDictionary = set(words)
        cache = {}
        return [word for word in words if self._canForm(word, wordDictionary, cache)]

    def _canForm(self, word, wordDictionary, cache):
        if word in cache:
            return cache[word]
        for index in range(1, len(word)):
            prefix = word[:index]
            suffix = word[index:]
            if prefix in wordDictionary:
                if suffix in wordDictionary or self._canForm(suffix, wordDictionary, cache):
                    cache[word] = True
                    return True
        cache[word] = False
        return False


# input = ['cat', 'cats', 'dog', 'catsdog']
input = ['cat', 'cats', 'dog', 'catsdog']
print(Solution().findAllConcatenatedWords(input))
