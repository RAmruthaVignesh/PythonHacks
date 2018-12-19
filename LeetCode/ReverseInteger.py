class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        try:
            neg= False
            x_string= str(x)
            x_list= list(x_string)
            if x_list[0]== "-":
                del x_list[0]
                neg = True
            rev_list = list(reversed(x_list))
            if neg == True:
                rev_list = ["-"]+rev_list
            x_rev = int("".join(rev_list))
            if(x_rev>0) & (x_rev == x_rev & 0x7fffffff):
                return x_rev
            elif((x_rev<0) & ((x_rev& -0x80000000) == -0x80000000)):
               return x_rev
            else:
                return 0
            
        except:
            pass
            return 0
            
        
mysolution = Solution()
rev_int = mysolution.reverse(1534236469)
print rev_int