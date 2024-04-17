import random


def calculate_hand_value(hand):
    value = sum(hand)
    if 11 in hand and value > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def display_game(player_hand, dealer_hand, player_score, dealer_score, game_over=False):
    print("\n===== Blackjack =====")
    print(f"Player Hand: {player_hand} ({calculate_hand_value(player_hand)})")
    print(f"Dealer Hand: {dealer_hand} ({calculate_hand_value(dealer_hand)})")
    
    if game_over:
        print("\nGame Over!")
        print(f"Player Score: {player_score}")
        print(f"Dealer Score: {dealer_score}")
        if player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

def start_game():
    player_score = 0
    dealer_score = 0

    
    while True:
        player_hand = [random.randint(1, 11), random.randint(1, 11)]
        dealer_hand = [random.randint(1, 11), random.randint(1, 11)]

        while True:
            display_game(player_hand, dealer_hand, player_score, dealer_score)
            action = input("Do you want to hit or stand? ").lower()

            if action == 'h':
                player_hand.append(random.randint(1, 11))
                if calculate_hand_value(player_hand) > 21:
                    display_game(player_hand, dealer_hand, player_score, dealer_score, game_over=True)
                    print("Bust! You went over 21. Dealer wins this round.")
                    dealer_score += 1
                    break
            elif action == 's':
                while calculate_hand_value(dealer_hand) < 17:
                    dealer_hand.append(random.randint(1, 11))
                display_game(player_hand, dealer_hand, player_score, dealer_score, game_over=True)
                if calculate_hand_value(dealer_hand) > 21:
                    print("Dealer busts! You win this round.")
                    player_score += 1
                elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
                    print("You win this round!")
                    player_score += 1
                elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
                    print("Dealer wins this round.")
                    dealer_score += 1
                else:
                    print("It's a tie!")
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    start_game()
