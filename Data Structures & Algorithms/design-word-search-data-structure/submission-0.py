class TrieNode:

    def __init__(self):
        self.children = {}
        self.lastLetter = False

class WordDictionary:

    def __init__(self):
        self.dictionary = TrieNode()

    def addWord(self, word: str) -> None: 
        curr = self.dictionary
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.lastLetter = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.lastLetter
            if word[index] != ".":
                if word[index] in node.children:
                    return dfs(index + 1, node.children[word[index]])
                return False
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(index+1, child):
                        return True
                return False

        return dfs(0, self.dictionary)