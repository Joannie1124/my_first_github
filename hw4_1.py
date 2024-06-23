import random
ranks=['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']
suits=['CLUB','HEART','DIAMOND','SPADE']

deck=[]
for s in suits:
	for r in ranks:
		deck.append(s+' '+r)
random.shuffle(deck)

player_card=''
for i in range(2):
	card=random.choice(deck) #CLUB 4 HEART 5
	player_card+=card

player_card=player_card.split(" ")
point=int(player_card[1])+int(player_card[3])
print(point)






	