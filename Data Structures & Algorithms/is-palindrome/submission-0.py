class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_list = list(s)
        frontPointer = 0
        backPointer = len(s)- 1

        while frontPointer < backPointer:
            while frontPointer < backPointer and not s[frontPointer].isalnum():
                frontPointer += 1

            while frontPointer < backPointer and not s[backPointer].isalnum():
                backPointer -= 1

            if s[frontPointer].lower() != s[backPointer].lower():
                return False
            
            frontPointer += 1
            backPointer -= 1
        
        return True




