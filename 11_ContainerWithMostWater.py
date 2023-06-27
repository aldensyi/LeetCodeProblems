# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Two Pointer Question

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area  = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res

# BF way: O(n^2), where you have double for loops to attain every volume possible with the given array.
        # res = 0
        
        # for l in range(len(height)):
        #     for r in range (l+1, len(height)):
        #         # r - l is the length aka the distance from initial pointer to current pointer
        #         area = (r - l) * min(height[l], height[r]) # min will help choose the shorter one for area, as it cannot overflow
        #         res = max(res, area) # set highest to result

        # return res

    # Exceeds Time Limit

# Two Pointer Technique
    # We have each pointer at the very end and then slowly bring both of them in 
    # O(n) aka Linear Time Complexity