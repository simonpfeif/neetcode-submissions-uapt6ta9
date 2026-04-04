class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = deque()
        starStack = deque()

        for i, c in enumerate(s):
            if c == '(':
                leftStack.append(i)
            elif c == '*':
                starStack.append(i)
            else: # right parenthesis
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        
        while leftStack and starStack:
            if leftStack[-1] > starStack[-1]:
                return False
            leftStack.pop()
            starStack.pop()
        
        if leftStack:
            return False
        else:
            return True
                    