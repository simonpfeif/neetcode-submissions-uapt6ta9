# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # first pass - find the first person that knows no one
        # - build adj list cache
        # - if we find no person that knows no one, return -1
        celebrity = -1
        for i in range(n):
            flag = True
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    flag = False
                    break
            if flag:
                celebrity = i
                break

        if celebrity == -1:
            return -1

        # Second pass - check if every person knows the potential celebrity
        # - Use the adj list cache to not repeat knows() calls
        # - if anyone does not know the potential celebrity, return -1
        # - if everyone knows the celebrity, return the celebrity

        for i in range(n):
            if i == celebrity:
                continue

            # add cache?
            if not knows(i, celebrity):
                return -1
        
        return celebrity