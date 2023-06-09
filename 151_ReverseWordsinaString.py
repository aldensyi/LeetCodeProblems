# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        res.reverse()
        return " ".join(res)

# Other ways that I can solve this problem
# - Via [::-1] -> Slicing with a step of -1 meaning it will create a list where it will step -1 (aka backwards) and iterate through the
#                   whole list
# - Via a for loop and reversed() -> run a for loop like "for x in ___" but in the blank we use (reversed("whatever list one is 
#                                    trying to reverse and iterate through")) and then appened the contents into a new list