# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = p[1] * (len(nums))

        # essentially you want the multiplication sum of everything before the value we are going over and the sum of multiplication after it 
        # best way to approach it while keeping O(n) is through pre and post fix
        # going through the first for loop will allow the sum of the multiplication of the everything before the actual value will be stored
        # ex) 1,2,3,4
        #  = 1, 1, 2, 6
        # going through the second for loop will allow for the sum of the multiplication of everything after the actual value will be stored
        # ex) 1,2,3,4
        #  = 24, 12, 4, 1
        # multiply those two together and one should get the the requested array of [24, 12, 8, 6]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # instead of storing it separate array, traversing backwards and multiplying the results into result array
            postfix *= nums[i]
        return res

# HAVE TO WRITE IT IN O(n) TIME
# Use prefix and postfix = two for loops: one for prefix and one for postfix