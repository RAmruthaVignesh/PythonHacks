#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx,val in enumerate(nums):
            # if target-val in nums[idx+1:len(nums)]:
            #     return [idx, nums.index(target-val,1)]
            #     break
            try:
                temp=0
                to_return = [idx, nums.index(target-val)]
                while idx == nums.index(target-val,temp):
                    temp=temp+1
                    to_return = [idx, nums.index(target-val,temp)]
                return to_return
                break
            except:
                pass

mysolution = Solution()
indices= mysolution.twoSum([5,5,11], 10)
print indices