class Solution:
    def wordBreak(self, input_string: str, wordDict: List[str]) -> List[str]:
        memory = {}
        possible_sentences = set()

        stack = []
        stack.append(([], 0))  # current sentance, current index

        max_length = 0
        for word in wordDict:
            max_length = max(max_length, len(word))

        while stack:
            current_sentence, current_index = stack.pop()
            # print(current_sentence)

            if current_index not in memory:
                memory.setdefault(current_index, [])
                for word in wordDict:
                    if input_string.startswith(word, current_index):
                        memory[current_index].append([word])
                        # temp_index = 0
                        # temp_sentence = current_sentence + [word]
                        # for i, word in enumerate(temp_sentence):
                        #     memory[temp_index].append(temp_sentence[i:])
                        #     temp_index += len(word)

            for word in memory[current_index]:
                new_sentence = current_sentence + word
                new_index = current_index + len("".join(word))
                if new_index == len(input_string):
                    print(new_sentence)
                    possible_sentences.add(" ".join(new_sentence))
                else:
                    stack.append((new_sentence, new_index))

        return possible_sentences
