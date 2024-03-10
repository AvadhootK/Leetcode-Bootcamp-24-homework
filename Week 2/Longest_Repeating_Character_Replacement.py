class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, maxp = 0,0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxp = max(maxp,count[s[r]])
            
            if (r-l+1) - maxp > k:
                count[s[l]] -= 1
                l += 1
        return (r - l + 1)