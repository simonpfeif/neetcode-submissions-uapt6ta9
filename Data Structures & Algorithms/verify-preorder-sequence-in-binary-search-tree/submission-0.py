class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        # key insight -> we know the min value possible for a valid tree
        # every time we "move right" we pop from the stack, and update our new min
        # every time we "move left" we add to the stack

        stack = []
        min_limit = float('-inf')

        for num in preorder:
            while stack and num > stack[-1]:
                min_limit = stack.pop()
            
            if num <= min_limit:
                return False
            
            stack.append(num)
        
        return True

    
    #     5
    # 2       6
    #       1
    #         3