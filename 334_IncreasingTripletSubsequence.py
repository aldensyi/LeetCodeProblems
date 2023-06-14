# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []

        for num in nums:
            # essentially finds the leftmost insert point within the list given for the value given
            # in this case: leftmost insert point of num in dp
            idx = bisect_left(dp, num)
            
            # if there is none in the dp: it will fill it as 1 or anything is greater than 0
            # if there is something:
                # but idx is smaller than the length:  whatever idx the number needs to be inserted and replace with it
                # but idx is bigger than the length: then we will append it to the end

            
            if index < len(dp):
                dp[index] = num
            else:
                dp.append(num)

            # if there is three consecutive numbers then we are going to return true
            if len(dp) > 2:
                return True

        # otherwise false
        return False



# Using DP
# time complexity: O(nlogn)
# using bisect_left - 