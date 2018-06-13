from string import maketrans
from string import translate
# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). T
# he output should be true or false representing whether the robot makes a circle.
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        iscircle = False
        pos= {"L" : [1,0] , "R":[-1,0], "U": [0,1], "D": [0,-1]}
        init = [0,0]
        moves = list(moves)
        
        

        # swapReturnPath= maketrans("UL", "DR")
        # swapped_moves = moves.translate(swapReturnPath)
        # if len(set(swapped_moves)) == len(set(moves))/2:
        #     iscircle = True
        # return iscircle
        
mysolution = Solution()
iscircle = mysolution.judgeCircle("LLLLRRRL")
print iscircle
