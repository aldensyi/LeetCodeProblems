# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# More like a medium question
# difficult part: edge cases

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Taking in the array and adding 0 at the ends
        f = [0] + flowerbed + [0]

        # Iterating through and checking if there are three consecutive empty spots
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0  # if there are more than n spots available it will always return true
    

        # Alternate solution
        # empty = 0 if flowerbed[0] else 1  # Using the variable empty to keep track of how many empty contiguous spots there are
        # for f in flowerbed:s
        #    if f:  # if we do see a flower
        #       n -= int((empty - 1) / 2) # int division, round towards zero
        #       empty = 0
        #    else:
        #       empty += 1
        # n -= (empty) // 2
        # return n <= 0 

        
# Time complexity: O(n)
# Space complexity: O(1)

# Taking in the array and adding 0 at the ends
# Iterate through the original values of the array