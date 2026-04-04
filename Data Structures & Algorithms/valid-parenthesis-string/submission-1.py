class Solution:
    def checkValidString(self, s: str) -> bool:

        leftMin, leftMax = 0, 0

        for i, c in enumerate(s):
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
            
        return leftMin == 0
                

        # leftStack = deque()
        # starStack = deque()

        # for i, c in enumerate(s):
        #     if c == '(':
        #         leftStack.append(i)
        #     elif c == '*':
        #         starStack.append(i)
        #     else: # right parenthesis
        #         if leftStack:
        #             leftStack.pop()
        #         elif starStack:
        #             starStack.pop()
        #         else:
        #             return False
        
        # while leftStack and starStack:
        #     if leftStack[-1] > starStack[-1]:
        #         return False
        #     leftStack.pop()
        #     starStack.pop()
        
        # if leftStack:
        #     return False
        # else:
        #     return True
                    