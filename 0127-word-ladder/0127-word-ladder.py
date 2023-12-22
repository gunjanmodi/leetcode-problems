class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        word_set = set(word_list)
        if end_word not in word_set:
            return 0

        k = len(begin_word)
        word_chars_reference = [set() for _ in range(k)]
        for word in word_list:
            for i in range(k):
                word_chars_reference[i].add(word[i])

        queue = collections.deque([begin_word])
        transformations = 0
        visited = set()

        while queue:
            queue_length = len(queue)
            transformations += 1
            
            for _ in range(queue_length):
                current_word = queue.popleft()

                if current_word == end_word:
                    return transformations

                visited.add(current_word)
                current_word_list = [c for c in current_word]

                for i in range(k):
                    for c in word_chars_reference[i]:
                        current_letter = current_word_list[i]
                        current_word_list[i] = c
                        next_word = ''.join(current_word_list)
                        if next_word in word_set and next_word not in visited:
                            queue.append(next_word)
                        current_word_list[i] = current_letter
        return 0

        