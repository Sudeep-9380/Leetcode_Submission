class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left=0
        window_size=0
        ans=float('-inf')
        for right in range(len(nums)):
            window_size+=nums[right]
            if right-left+1==k:
                ans=max(ans,window_size/k)
                window_size-=nums[left]
                left+=1
        return ans

        