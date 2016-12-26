#main game rules
# rock and paper - paper wins
#scissors and paper - scissors wins
#check for ties and invalid input
def game_rules(ip_player1,ip_player2):
    ip = ["rock", "scissors", "paper"]
    #check if the inputs are valid
    if ((ip_player1== ip[0] or ip_player1==ip[1] or ip_player1==ip[2]) and  (ip_player2== ip[0] or ip_player2==ip[1] or ip_player2==ip[2])):
        if(ip_player1==ip_player2):
            return "It is a tie game"
        elif((ip_player1==ip[0] and ip_player2==ip[1]) or (ip_player1==ip[1] and ip_player2==ip[2]) or (ip_player1 ==ip[2] and ip_player2==ip[0])):
            return "congrats player 1"
        else:
            return "congrats player 2"
    else:
        return "Invalid input"

def get_input():
    p1 = raw_input("Enter player 1 input")
    p2 = raw_input("Enter player 2 input")
    print game_rules(p1,p2)

get_input()



