import random

# Function to create a deck of cards
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    return [f"{rank} of {suit}" for rank in ranks for suit in suits]

# Function to calculate hand value
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card.split(" ")[0]
        if rank.isdigit():
            value += int(rank)
        elif rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11

    # Adjust for Aces if value exceeds 21
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value

# Function to display hand
def display_hand(player, hand):
    print(f"{player}'s hand: {', '.join(hand)} (Value: {calculate_hand_value(hand)})")

# Main game logic
def blackjack():
    deck = create_deck()
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    print("Welcome to Blackjack!")
    display_hand("Player", player_hand)
    print(f"Dealer's hand: {dealer_hand[0]}, Hidden")

    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == 'hit':
            player_hand.append(deck.pop())
            display_hand("Player", player_hand)
        elif choice == 'stand':
            break
        else:
            print("Invalid choice, please choose 'hit' or 'stand'.")

    player_value = calculate_hand_value(player_hand)
    if player_value > 21:
        print("Player busts! Dealer wins.")
        return

    # Dealer's turn
    print("\nDealer's turn:")
    display_hand("Dealer", dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        print("Dealer hits.")
        dealer_hand.append(deck.pop())
        display_hand("Dealer", dealer_hand)

    dealer_value = calculate_hand_value(dealer_hand)
    if dealer_value > 21:
        print("Dealer busts! Player wins.")
        return

    # Determine the winner
    print("\nFinal Results:")
    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand)

    if player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    blackjack()
