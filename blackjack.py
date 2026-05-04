
import random
def main():
    cards = []
    player_hand = []
    suits =["spades", "clubs", "hearts", "diamonds"]
    ranks =["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for suit in suits:
        for rank in ranks:
            cards.append([suit, rank])


    def game():
        value, i, j = 0, 0, 1 
        while value < 21:
            player_response = input("Do you want a card ?")
            if player_response == "yes":
                card = random.choice(cards)
                player_hand.append(card)
                cards.remove(card)
                rank =player_hand[i][j]
                if rank == "A" and value == 20:
                    value +=1
                elif rank == "A" and value != 20:
                    value += 11
                elif rank == "K" or rank == "Q" or rank == "J" :
                    value += 10
                else:
                    value += int(rank)
                print(player_hand , value)
            else:
                break
            i += 1

        if value == 21:
            return "YOU WON !"
        else : 
            return "Maybe another time"      


    print(game())

if __name__ == "__main__":
    main()
  