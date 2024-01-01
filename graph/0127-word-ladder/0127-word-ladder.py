class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        word_set.add(beginWord)
        if endWord not in word_set:
            return 0

        k = len(beginWord)
        word_chars_reference = [set() for _ in range(k)]
        for word in wordList:
            for i in range(k):
                word_chars_reference[i].add(word[i])

        queue = collections.deque([beginWord])
        transformations = 0
        visited = set([beginWord])

        while queue:
            queue_length = len(queue)
            transformations += 1
            
            for _ in range(queue_length):
                word = queue.popleft()

                if word == endWord:
                    return transformations

                for i in range(k):
                    first_part, last_part = word[:i], word[i+1:]
                    for c in word_chars_reference[i]:
                        next_word = f'{first_part}{c}{last_part}'
                        if next_word in word_set and next_word not in visited:
                            queue.append(next_word)
                            visited.add(next_word)
        return 0
