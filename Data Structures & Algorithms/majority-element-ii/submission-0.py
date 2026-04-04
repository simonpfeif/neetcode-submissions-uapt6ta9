class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = collections.defaultdict(int)
        target = len(nums) / 3 
        
        for n in nums:
            hashMap[n] += 1
        
        res = []
        
        for key, val in hashMap.items():
            if val > target:
                res.append(key)
            
        return res