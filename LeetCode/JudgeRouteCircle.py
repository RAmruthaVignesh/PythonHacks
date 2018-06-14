# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). T
# he output should be true or false representing whether the robot makes a circle.
from operator import add
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
        temp = init
        for curr_move in moves:
            final_pos= list(map(add, temp, pos[curr_move]))
            temp= final_pos
        if final_pos == [0,0]:
            return True
        else:
            return False    
mysolution = Solution()
iscirclepath = mysolution.judgeCircle("LLLLRRRL")
print iscirclepath
