import random

# give_card = 2
# deck = []
# num = [1,2,3,4,5,6,7,8,9,10]
# col = ['red', 'blue', 'green', 'yellow']

# for i in range(give_card):
#     card = [num[random.randint(0,len(num)-1)], col[random.randint(0,len(col)-1)]]
#     deck.append(card)

play = [0]

class Uno:
    
    # def __init__(self):
        
    def deal(self):
        
        give_card = 7
        deck = []
        num = [1,2,3,4,5,6,7,8,9,10]
        col = ['red', 'blue', 'green', 'yellow']
        
        for i in range(give_card):
            card = [num[random.randint(0,len(num)-1)], col[random.randint(0,len(col)-1)]]
            deck.append(card)
            
        self.hand = deck
        
    def take(self):
        give_card = 1
        deck = []
        num = [1,2,3,4,5,6,7,8,9,10]
        col = ['red', 'blue', 'green', 'yellow']
        
        for i in range(give_card):
            card = [num[random.randint(0,len(num)-1)], col[random.randint(0,len(col)-1)]]
            deck.append(card)
        self.hand.append(deck)
    
    def place(self, num):
        
        
        play.insert(0,self.hand[num-1])
        self.hand.remove(self.hand[num-1])
    
    
    
    
    
    
    
        
    def __repr__(self):
        return f'{self.hand}'
