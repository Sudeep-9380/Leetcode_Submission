class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
       
        right=len(s)-1
        for i in range(0,len(s),2*k):
            left=i
            right = min(i + k - 1, len(s) - 1)

            while left<right:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)
