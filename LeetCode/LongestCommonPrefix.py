# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count = len(strs)
        prefix = ""
        if len(strs)>0:
            if strs[0]:
                temp = strs[0][0]
                try:
                    for i in range(len(strs[0])): # loop through every item in string
                        temp_pass = ""
                        for curr_item in range(count): # looping through length of the string
                            if temp == strs[curr_item][i]: # compare every item in all the strings
                                temp_pass = temp
                            else:
                                temp_pass= ""
                                break
                        if temp_pass== "":
                            break
                        prefix = prefix+temp_pass
                        temp = strs[0][i+1]
                except (NameError, IndexError):
                    pass
                return prefix
            else:
                return prefix
        else:
            return prefix            
mysolution = Solution()
common_prefix= mysolution.longestCommonPrefix(["fling", "fwift", " "])
print common_prefix
