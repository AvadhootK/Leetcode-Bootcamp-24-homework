class Solution:
    def maxArea(self, height: List[int]) -> int:
        # volume (x*y) should be maximum
        # n = len(height)
        # index of array - x axis
        # value of i - y axis
        # (x2-x1) * min(y1,y2) -> max

        # # brute force
        # max = 0
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         k = ((j+1)-(i+1))*min(height[i],height[j])
        #         if k > max:
        #             max= k
        # return max
        # # time limit exceeded


        # 2 pointer
        left = 0
        right = len(height)-1
        max = 0
        while left<right:
            minimum = min(height[left],height[right])
            k = (right-left)*minimum
            if k>max:
                max =k
            if minimum==height[left]:
                left+=1
            else:
                right-=1
        return max
            


