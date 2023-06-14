#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}


# In[2]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank.capitalize()]
        
    def __str__(self):
        return self.rank+" of "+self.suit
        
        
    


# In[3]:


two_clubs = Card('Clubs','two')  


# In[4]:


class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                create_card = Card(suit,rank)
                self.all_cards.append(create_card)
    
                
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


# In[5]:


print(Deck().all_cards[-1])


# In[6]:


class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    
    def new_card(self,add_card):
        if type(add_card) == type(self.all_cards):
            self.all_cards.extend(add_card)
        else:
            self.all_cards.append(add_card)
    def remove_card(self):
        return self.all_cards.pop(0)
    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards'


# In[7]:


ndanga = Player('Ndanga')


# In[ ]:





# In[8]:


ndanga.new_card(Deck().all_cards[0])


# In[9]:


print(ndanga)


# In[10]:


#GAME SETUP

player1 = Player('One')
player2 = Player('Two')

deck = Deck()
deck.shuffle_deck()

for i in range(26):
    player1.new_card(deck.deal_one())
    player2.new_card(deck.deal_one())


# In[11]:


print(player1.all_cards[0])


# In[12]:


print(len(player2.all_cards))


# In[13]:


game = True
round_number = 0
while game:
    round_number += 1
    print(f'Round {round_number}')
    
    if len(player1.all_cards) == 0:
        print('Player1 is out of cards, Player 2 WINS!')
        game = False
        break
    if len(player2.all_cards) == 0:
        print('Player2 is out of cards, Player 1 WINS!')
        game = False
        break
        
        #NEW ROUND
        
    player_1_card = []
    player_2_card = []
        
    player_1_card.append(player1.remove_card())
    player_2_card.append(player2.remove_card())
        
        #WAR
    at_war = True
    
    while at_war:
        
        if player_1_card[-1].value > player_2_card[-1].value:
            
            player1.new_card(player_2_card)
            player1.new_card(player_1_card)
            
            at_war = False
            
        elif player_1_card[-1].value < player_2_card[-1].value:
            
            player2.new_card(player_2_card)
            player2.new_card(player_1_card)
            
            at_war = False
            
        else:
            print('WAR!!!!!!!')
            
            if len(player1.all_cards)<3:
                print('Unable to declare war, player two won')
                game = False
                break
            elif len(player2.all_cards)<3:
                print('Unable to declare war, player one won')
                game = False
                break
                
            else:
                for i in range(3):
                    player_1_card.append(player1.remove_card())
                    player_2_card.append(player2.remove_card())
            
        


# In[ ]:




