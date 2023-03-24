from random import randint, choice, shuffle

# Card class
class card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

# Deck class made of cards
class deck():
    def __init__(self, jokers=False):
        self.jokers = jokers
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = [str(i) for i in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
        self.cards = [card(suit, value) for suit in self.suits for value in self.values]
        if self.jokers:
            self.cards += [card("Joker", "Joker") for i in range(2)]
    
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
    
    def __iter__(self):
        return iter(self.cards)
    
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, index):
        return self.cards[index]
    
    # Shuffles the deck
    def shuffle(self):
        return shuffle(self.cards)
    
    # Picks a random card from the deck without replacement
    def pick_card(self):
        if not self.cards:
            raise ValueError("All cards have been picked")
        return self.cards.pop(randint(0, len(self)-1))
    
    # Picks a random card from the deck with replacement
    def pick_card_with_replacement(self):
        if not self.cards:
            raise ValueError("All cards have been picked")
        return choice(self)

# Player class
class player():
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def __repr__(self):
        return f"Player {self.name} has {len(self.hand)} cards"
    
    def __len__(self):
        return len(self.hand)
    
    def __getitem__(self, index):
        return self.hand[index]
    
    # Draws variable amount of (default 1) cards from the deck
    def draw(self, deck, amount=1):
        for i in range(amount):
            self.hand.append(deck.pick_card())
    
    # Discards a card from the player's hand
    def discard(self, index):
        return self.hand.pop(index)
    
# Game class
class game():
    def __init__(self, num_players, num_decks=1, jokers=False):
        # Allows the user to input the name of each player
        self.players = []
        for i in range(0, num_players):
            self.players.append(player(input(f"What is player {i+1}'s name? ")))
        self.deck = deck(jokers)
        for i in range(0, num_decks-1):
            self.deck.cards += deck(jokers).cards
        self.deck.shuffle()
    
    def __repr__(self):
        return f"Game with {len(self.players)} players"
    
    def __len__(self):
        return len(self.players)
    
    def __getitem__(self, index):
        return self.players[index]
    
    # Deals a variable amount of (default 1) cards to each player
    def deal(self, amount=1):
        for player in self.players:
            player.draw(self.deck, amount)

# test_deck = deck(jokers=True)
# print(test_deck.pick_card_with_replacement())

# test_game = game(2, 2, True)
# test_game.deal(26)
# print(test_game.players)
# print(test_game.deck)