# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        # isDivisor is a helper function that helps checking if the substring created is a factor for both str1 and str2
        # l: given/passed in length
        def isDivisor(l):
            # checking if l is a factor for both strings
            if len1 % l or len2 % l:
                return False

            # building the string
            # f1 and f2 are the substring factors of the string aka how many time we need to multiply the substring to recreate str1 and str2
            f1, f2 = len1 // l, len2 // l
            # checking if it can be recreated, if yes the return the substring, if no then it will not return anything
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        # iterating down for greedy
        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""


# Brute:
# need an x that can create both of the string; the value of the substring can not be something that can create one but not the other
# aka L1(length of str1 or str2) % substring == 0

# Greedy:
# starting with the shorter string and seeing if it can fit into the the longer string

# Time complexity of the problem is:
# O(min(m,n))