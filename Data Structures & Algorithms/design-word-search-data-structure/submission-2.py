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
            #Base Case
            if index == len(word):
                return node.lastLetter
            
            #Two possible node, either a letter or a "."
            #Dots can be matched with any letter, meaning theres 26 possible paths from a single dot, we need DFS to backtrack
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(index+1, child):
                        return True
                return False
            # Not a dot, we just iterate normally checking if the letter exist in dictionary or not
            if word[index] != ".":
                if word[index] in node.children:
                    #to iterate to next letter, we move the index up just like a for letter in word in a Trie
                    return dfs(index + 1, node.children[word[index]])
                return False

        return dfs(0, self.dictionary)