import random

class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        # Assume a deck with more face cards (2x more face cards than number cards)
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = cards * 4 + cards * 8  # Twice as many face cards
        return [(card, suit) for card in deck for suit in suits]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)
        return card

    def calculate_hand_value(self, hand):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        total_value = sum(values[card[0]] for card in hand)
        # Adjust for Aces
        for card in hand:
            if card[0] == 'A' and total_value > 21:
                total_value -= 10
        return total_value

    def display_hand(self, hand, hide_first_card=False):
        if hide_first_card:
            print(f"Hidden Card, {hand[1]}")
        else:
            print(', '.join(map(lambda x: f"{x[0]} of {x[1]}", hand)))

    def play(self):
        self.shuffle_deck()

        # Initial deal
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        # Player's turn
        while True:
            print("\nPlayer's Hand:")
            self.display_hand(self.player_hand)
            player_value = self.calculate_hand_value(self.player_hand)

            if player_value == 21:
                print("Blackjack! You win!")
                break

            if player_value > 21:
                print("Bust! You lose.")
                break

            action = input("Do you want to hit or stand? ").lower()
            if action == 'hit':
                self.deal_card(self.player_hand)
            elif action == 'stand':
                break
            else:
                print("Invalid input. Please enter 'hit' or 'stand'.")

        # Dealer's turn
        print("\nDealer's Hand:")
        self.display_hand(self.dealer_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        while dealer_value < 17:
            self.deal_card(self.dealer_hand)
            dealer_value = self.calculate_hand_value(self.dealer_hand)

        print("\nFinal Results:")
        print("\nPlayer's Hand:")
        self.display_hand(self.player_hand)
        print(f"Player's Hand Value: {self.calculate_hand_value(self.player_hand)}")

        print("\nDealer's Hand:")
        self.display_hand(self.dealer_hand)
        print(f"Dealer's Hand Value: {dealer_value}")

        # Determine the winner
        if dealer_value > 21:
            print("Dealer bust! You win!")
        elif player_value > 21:
            print('You bust! Dealer wins!')
        elif player_value > dealer_value and player_value <= 21:
            print("You win!")
        elif player_value < dealer_value and dealer_value <= 21:
            print("You lose.")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    blackjack_game = BlackjackGame()
    blackjack_game.play()
