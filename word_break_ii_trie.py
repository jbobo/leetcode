class TrieNode:
    def __init__(self, val, is_end=False):
        self.val = val
        self.is_end = is_end
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        if not word:
            return

        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.is_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.word_break(s, wordDict)

    def word_break(self, seq, word_dict):
        # Construct trie
        trie = Trie()
        for word in word_dict:
            trie.insert(word)

        return self.walk(seq, trie.root, {})

    def walk(self, seq, root, memo):
        if not seq:
            return ['']
        if seq in memo:
            return memo[seq]

        # Find all the words we can get from the beginning of seq
        # E.g. for 'catsanddogs', this would be ['cat', 'cats']
        words = []
        curr = root
        for idx, char in enumerate(seq):
            if char not in curr.children:
                break
            curr = curr.children[char]
            if curr.is_end:
                # Break point
                words.append(seq[: idx + 1])

        fragments = []
        for word in words:
            # Recurse using substring of seq after word,
            # which is necessarily a prefix.
            # E.g. if seq=`catsanddogs` and word=`cats`,
            # recursive with seq'='anddogs'.
            rest_of_sentence_endings = self.walk(
                seq[len(word):], root, memo
            )
            # Join each of the returned setence endings to
            # create a new, longer set of sentence endings.
            for sentence_ending in rest_of_sentence_endings:
                if sentence_ending:
                    fragments.append(' '.join([word, sentence_ending]))
                else:
                    fragments.append(word)

        memo[seq] = fragments
        return memo[seq]
