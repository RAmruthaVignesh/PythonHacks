#main game rules
# rock and paper - paper wins
#scissors and paper - scissors wins
#check for ties and invalid input
def game_rules(ip_player1,ip_player2):
    ip = ["rock", "scissors", "paper"]
    winning_combo = [["paper","rock"], ["scissors","paper"], ["rock","scissors"]]
    #check if the inputs are valid
    if (ip_player1.lower() in ip) and (ip_player2.lower() in ip):
        if ip_player1 == ip_player2:
            return "It is a tie game"
        elif([ip_player1,ip_player2] in winning_combo):
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

