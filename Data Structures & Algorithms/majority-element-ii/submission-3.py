class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = collections.defaultdict(int)
        
        for n in nums:
            hashMap[n] += 1

            if len(hashMap) < 3:
                continue
            
            newHashMap = collections.defaultdict(int)
            for key, val in hashMap.items():
                if val > 1:
                    newHashMap[key] = val - 1
            hashMap = newHashMap
                
        res = []
        for key, val in hashMap.items():
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        return res