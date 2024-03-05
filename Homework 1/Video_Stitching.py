class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 2 pointer - start and end of current clip
        # sort clips 
        clips = sorted(clips)
        # print(clips)
        # i is start, j is end
        start = -1
        end = 0
        res = 0
        for i,j in clips:
            if end>=time or i>end:
                break
            elif start <i <=end:
                res+=1
                start = end
            end = max(end,j)
        if end>=time:
            return res
        else:
            return -1