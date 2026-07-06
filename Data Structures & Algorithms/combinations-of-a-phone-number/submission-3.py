class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def helper(i, curComb): #curComb = ""
            #Base Cases
            if i == len(digits): #We've reached last index, meaning len(curComb) == len(digits), so each digit has a corresponding letter now, add that combination to results
                result.append(curComb)
                return
            if i > len(digits): #Tech deadcode since first base case will always hit before we reach this
                return
            
            for c in digit_to_char[digits[i]]: #For every character in a digit, make a combination with the next digit's characters, and following etc like a tree
                helper(i+1, curComb + c) #We dont need to pop strings after adding because they are immutable, each pass is a new string version

        helper(0, "")
        return result

        
#This is a good tree illustration of whats happening
    #                  (i=0, cur="")
    #                 /      |      \
    #                /       |       \
    #           (i=1,"a") (i=1,"b") (i=1,"c")
    #           /  |  \    /  |  \    /  |  \
    #          /   |   \  /   |   \  /   |   \
    # (i=2,"ad") (ae) (af) (bd) (be) (bf) (cd) (ce) (cf)
    #   (leaf)   (leaf) (leaf) (leaf) (leaf) (leaf) (leaf) (leaf) (leaf)