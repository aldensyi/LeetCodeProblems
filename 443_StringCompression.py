
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0       # first index of the current group
        res = 0     # length of the answer
        while i < len(chars):
            # assuming that there is at least one of the specified letter; set group length to 1
            group_length = 1
            
            # while current index + the length of the group is smaller than the length of the whole string,
            # and current group length + current index's character the same as the current index's character
            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                # you add a length to the group to signify the length of the group
                group_length += 1
            chars[res] = chars[i]
            res += 1
            # if group length is bigger than one which will only apply if there is more than one of the character specified
            if group_length > 1:
                # int storing length of the answer is changed into string
                str_repr = str(group_length)
                # add how long the length of the specific letter we were counting onto chars
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            # increase i by groupLength and proceed to the next 
            i += group_length
        return res