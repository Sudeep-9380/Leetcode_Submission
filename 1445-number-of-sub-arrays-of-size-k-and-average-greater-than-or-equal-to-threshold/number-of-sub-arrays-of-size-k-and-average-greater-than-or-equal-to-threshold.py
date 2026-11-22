class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left=0
        window_size=0
        ans=0
        for right in range(len(arr)):
            window_size+=arr[right]
            if right-left+1==k:
                if window_size/k>=threshold:
                    ans+=1
                window_size-=arr[left]
                left+=1
        return ans