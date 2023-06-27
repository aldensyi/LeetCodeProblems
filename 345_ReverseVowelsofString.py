# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Type of Question: Two Pointers
# just have two different pointer i, and j and increment up and down if it meets the req that the question is asking.
class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        i, j = 0, len(s)-1
        vowels = "aeiouAEIOU"

        while i < j:
            if lst[i] not in vowels:
                i += 1
            if lst[j] not in vowels:
                j -= 1
            if lst[i] in vowels and lst[j] in vowels:
                lst[i], lst[j] = lst[j], lst[i]
        return lst