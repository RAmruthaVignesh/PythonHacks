# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:].zfill(64)
        y = bin(y)[2:].zfill(64)
        pos = [i for i in range(len(x)) if x[i]!= y[i]]
        return len(pos)

mysolution = Solution()
hamming_distance = mysolution.hammingDistance(297630147,147274294)
print hamming_distance 