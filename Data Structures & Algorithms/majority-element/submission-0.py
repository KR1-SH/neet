class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for x in nums:
            if x not in count:
                count[x] = 0
            elif x in count:
                count[x] += 1
        
        max_key = max(count, key=count.get)
        return(max_key)
        