# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.
#   You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel = set(J)
        return sum([stone in jewel for stone in S])
        
mysolution = Solution()
num_jewels= mysolution.numJewelsInStones("aA", "aAAbbbb")
print num_jewels