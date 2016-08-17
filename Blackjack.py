# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = True
outcome = ""
score = 0
instruction = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
       
    def __str__(self):
        a = ""
        for i in self.hand:
            a += i[0] + i[1] + " "
        return "Hand contains " + a

    def add_card(self, card):
            # add a card object to a hand
        self.hand.append([card.get_suit(), card.get_rank()])

    def get_value(self): 
        self.value = 0
        ace = False   
        for i in self.hand:
            self.value += VALUES[i[1]]
            if i[1] == 'A':
                ace = True
        if (ace == True) and ((self.value + 10) <= 21):    
            self.value += 10           
        return self.value               
                      
    def draw(self, canvas, pos):
        i = 0 
        for card in self.hand:
            temp = Card(card[0],card[1])
            temp.draw(canvas,[50 + pos[0] * i, pos[1] * 2])
            i += 1
        
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append([suit,rank])

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):       
        deal = self.deck.pop()
        return Card(deal[0],deal[1])
            
    def __str__(self):
        a = ""
        for card in self.deck:
            a += card[0] + card[1] + " "
        return "Deck contains " + a
    
    
#define event handlers for buttons
def deal():
    global outcome, in_play, instruction,player_hand,dealer_hand, my_deck
    outcome = ""
    instruction = "Hit or Stand?"
    # your code goes here
    player_hand = Hand()
    dealer_hand = Hand()
    my_deck = Deck()
    my_deck.shuffle()
    player_hand.add_card(my_deck.deal_card())
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    in_play = True


def hit():
    global in_play, outcome, score, instruction,dealer_hand, my_deck
    if in_play:
        player_hand.add_card(my_deck.deal_card())    
        if player_hand.get_value() > 21:
            outcome = "You went bust and lose."
            instruction = "New deal?"
            in_play = False
            score -= 1
      
def stand():
    global outcome, instruction, in_play, score, dealer_hand, player_hand
    instruction = "New deal?"
    in_play = False
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(my_deck.deal_card())    
    if dealer_hand.get_value() > 21:
        outcome = "You win."
        score += 1
    elif dealer_hand.get_value() >= player_hand.get_value():
        outcome = "You lose."
        score -= 1
    elif dealer_hand.get_value() < player_hand.get_value():
        outcome = "You win."
        score += 1

# draw handler    
def draw(canvas):
    global dealer_hand, player_hand,in_play
    dealer_hand.draw(canvas,[CARD_SIZE[0] + 20, 110]) #y-values obtained by eye measures
    player_hand.draw(canvas,[CARD_SIZE[0] + 20, 220])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,\
                          [50 + CARD_CENTER[0],268],CARD_SIZE)
    
    canvas.draw_text(outcome,(280,175), 30, "Yellow")
    canvas.draw_text("Player",(110,400), 30, "Black")
    canvas.draw_text("Dealer",(110,175), 30, "Black")
    canvas.draw_text("Blackjack",(70,100), 50, "Turquoise")
    canvas.draw_text("Score:",(350,100), 30, "Black")
    canvas.draw_text(str(score),(440,100), 30, "Black")
    canvas.draw_text(instruction,(300,400), 30, "Black")
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
