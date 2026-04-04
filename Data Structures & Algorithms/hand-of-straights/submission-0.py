class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hashMap = Counter(hand)
        hand.sort()

        for num in hand:
            if hashMap[num]:
                for j in range(groupSize):
                    if not hashMap[num + j]:
                        return False
                    hashMap[num + j] -= 1
        
        return True