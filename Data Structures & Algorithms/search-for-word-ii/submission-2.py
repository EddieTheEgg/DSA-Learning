class TrieNode:
    def __init__(self):
        self.children = {} #max length of 26 character path for the chidl per letter
        self.isWord = False #Naturally most letters are not the end, but the last letter of words we set as True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #We first should build out tree, like as we iterate we
        # add our found letter to a children level but idk if
        # we should build our tree first or just iterate through

        #Step 1. First turn words list into a trie path
        trie_path = TrieNode()

        def insertWord(word : str):
            curr = trie_path
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isWord = True

        for word in words:
            insertWord(word)
        
        #Step 2: Backtracking through the grid and using out trie_path
        ROWS = len(board)
        COLS = len(board[0])

        valid_words = set()
        visit = set()

        def dfs(row, col, node, word):
            #Base case, a bad cell we need to backtrack up
            if row >= ROWS or col >= COLS or row < 0 or col < 0 or (row, col) in visit or board[row][col] not in node.children:
                return

            #Update current node/visited/word-being-built to the new cell we are now checking
            visit.add((row,col))
            node = node.children[board[row][col]]
            word += board[row][col]

            if node.isWord: #If the letter in the cell we are checking is a last letter, we've reached a word
                valid_words.add(word) # DO NOT EARLY RETURN, we could have bat and bats in the same path so keep checking
            
            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            #Remember to remove cell we've visited as we backtrack up
            #so we can try other directions
            visit.remove((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie_path, "")

        return list(valid_words)