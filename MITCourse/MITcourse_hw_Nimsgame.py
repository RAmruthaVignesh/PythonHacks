import random
def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
    stones = pile
    player = 1
    while(stones >= max_stones): #This is the loop that allows alternate player to pick stones
        x=random.randint(1,max_stones)
        print "player" , player , " picks", x , "stones"
        stones = stones - x
        print "The remaining stones in the pile is ", stones
        player = swapplayer(player)
    else:
        print "Game Over! player" , swapplayer(player) ,"wins"

def swapplayer(player):
    '''This function swaps the players'''
    if player == 1:
        player = 2
        return player
    else:
        player=1
        return player

play_nims(100,5)


    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#       
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over"