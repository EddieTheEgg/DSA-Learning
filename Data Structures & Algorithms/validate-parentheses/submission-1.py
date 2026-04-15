class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map: #If opening bracket, then add.
                stack.append(c)
                continue #breaks out of loop
            if not stack or stack[-1] != Map[c]: #If closing bracket, checks if stack is not empty first, then checks if last element of list matches the previous open bracket
                return False
            stack.pop()

        return not stack #in case stack is empty after popping.

        #([]) works.
        #({[]}) works
        #({)} fails since the open must close of the same.