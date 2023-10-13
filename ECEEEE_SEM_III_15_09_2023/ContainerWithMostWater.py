# Problem Link: https://leetcode.com/problems/container-with-most-water/
# We can split our approaches into optimal and bruteforce.

# Here's the bruteforce solution, as discussed during the session:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        for i,height1 in enumerate(height):
            for j,height2 in enumerate(height):
                area = (max(i,j)-min(i,j))*min(height1,height2)
                if area>maxarea:
                    maxarea = area
        return maxarea

# Here's the optimal solution, as discussed during the session:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg = 0
        end = len(height) - 1
        max_vol = 0

        while beg < end:
            vol = (end - beg) * min(height[beg], height[end])
            max_vol = max(max_vol, vol)

            if height[beg] < height[end]:
                beg += 1
            else:
                end -= 1

        return max_vol
