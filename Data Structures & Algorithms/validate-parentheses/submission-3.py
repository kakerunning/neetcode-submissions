class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = { ')':'(', '}': '{', ']':'['}

        for c in s :
            if c in close_to_open:
                if not stack or close_to_open[c] != stack[-1]: #s = ")"-> error out of index
                    return False
                else: 
                    stack.pop()
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False