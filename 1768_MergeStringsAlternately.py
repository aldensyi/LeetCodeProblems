# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        # better to keep res as a list and join them after to make a string
        res = []
        # idea: to run the loop until one of the words reaches out of bounds to where we can exit loop
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        
        # appened the rest of the word after exiting loop
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)

# How to approach:
# pointer for word1 and pointer for word2 and once one goes out of bounds, then append the rest
# Complexity of O(n+m)