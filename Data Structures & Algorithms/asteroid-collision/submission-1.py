class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            asteroid_broke = False
            while stack and stack[-1] > 0 and a < 0:
                if not stack:
                    stack.append(a)
                    break
                elif abs(a) < abs(stack[-1]):
                    asteroid_broke = True
                    break
                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                    asteroid_broke = True
                    break
                else:
                    stack.pop()
            if not asteroid_broke:
                stack.append(a)
        return stack



