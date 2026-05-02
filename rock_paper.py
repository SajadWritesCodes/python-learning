import random
def main():
    def get_choices():
        choices = ["Rock", "Paper", "Scissors"]
        player_choice =input("Enter your choice:")
        computer_choice = random.choice(choices)
        result = {"Player": player_choice, "Computer": computer_choice}

        return result
    result = get_choices()
    def winner(result):
        winner = "computer"
        if result["Player"] == result["Computer"]:
            winner = "It's a tie!"
        elif result["Player"] == "Rock" :
            if result["Computer"] == "Scissors" :
                winner = "Player"
        elif result["Player"] == "Siccors" :
            if result["Computer"] == "Paper":
                winner = "Player"                
        else:
            pass
        
        return winner

    final_result = winner(result)
    print(result, f"The winner is {final_result}")

if __name__ == '__main__':
    main()
