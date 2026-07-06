class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        #I think approach is, we take the digits, get all the corresponding letters
        # to each digit and combine to one string so for example 23 would be abcdef

        #Next, we do a combination, where we have total letters choose 2 letters so
        # abcdef would be len(string) so 6 choose 2 numbers since len(digits) was 2

        #Im gonna do this the binary iteraiton way but def can do it via loop as well
        # in the strings

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
        
        #So now we should have a string_to_process be "defghijkl"
        # Its a combination k choose n, where k is len(string_to_process) and n is amount of combinations for each digit so len(digits)

        def helper(i, curComb): #curComb = ""
            #Base Cases
            if len(curComb) == len(digits):
                result.append(curComb)
                return
            if i >= len(digits):
                return
            
            for c in digit_to_char[digits[i]]:
                helper(i+1, curComb + c)

        helper(0, "")

        return result
