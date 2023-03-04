class WordDictionary():
    def __init__(self):
        self.word_dict = collections.defaultdict(set)
    def addWord(self, word):
        self.word_dict[len(word)].add(word)
    def search(self, word):
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for w in self.word_dict[len(word)]:
            for i, c in enumerate(word):
                if c != '.' and c != w[i]:
                    break
            else:
                return True
        return False