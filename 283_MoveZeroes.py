# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # l is the index of the left-most zero element
        l = 0

        # r is traveral element
        for r in range(len(nums)):
            # if the element at the given array is a non-zero element
            if nums[r]:
                # you are swapping the left most zero with the given non-zero element
                nums[l], nums[r] = nums[r], nums[l]
                l += 1  # only increment the zero pointer aka the left pointer whenever you run into a non-zero element 
                        # as we are trying to keep the left-most zero
        

# could do with two separate arrays but can also partition using quicksort
# aka two pointers