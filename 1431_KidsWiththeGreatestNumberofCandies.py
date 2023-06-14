# There are n kids with candies.
# You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if,
# after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m_c = max(candies)
        return [x+extraCandies >= m_c for x in candies]

# can do one liner like this to where since the max candies is always defined, we can just iterate through via list comprehension
# [expression for variable in iterable(in this case: a list)]