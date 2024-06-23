

import random

element=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer=random.choice(element)#隨機從中抽一個作為正確答案

guess=input('Guess the lowercase alphabet: ')

tries=0 #嘗試(猜測)的次數

ad=0
eh=0
il=0
mp=0
qt=0
ux=0
yz=0
while guess != answer: #當猜測的不對時，進入迴圈不斷繼續猜測
	if guess>answer: #如果猜測的值在正確答案後面，則提示猜示要往前猜
		print("The alphabet you are looking for is alphabetically lower.")
		guess=input('Guess the lowercase alphabet: ')
		tries+=1
		#紀錄每次猜測的值都未於哪個區間裡面
		if guess in ['a','b','c','d']:
			ad+=1
		if guess in ['e','f','g','h']:
			eh+=1
		if guess in ['i','j','k','l']:
			il+=1
		if guess in ['m','n','o','p']:
			mp+=1
		if guess in ['q','r','s','t']:
			qt+=1
		if guess in ['u','v','w','x']:
			ux+=1
		if guess in ['y','z']:
			yz+=1

	if guess<answer: #如果猜測的值在正確答案前面，則提示猜示要往後猜
		print("The alphabet you are looking for is alphabetically higher.")
		guess=input('Guess the lowercase alphabet: ')
		tries+=1
	#紀錄每次猜測的值都未於哪個區間裡面
		if guess in ['a','b','c','d']:
			ad+=1
		if guess in ['e','f','g','h']:
			eh+=1
		if guess in ['i','j','k','l']:
			il+=1
		if guess in ['m','n','o','p']:
			mp+=1
		if guess in ['q','r','s','t']:
			qt+=1
		if guess in ['u','v','w','x']:
			ux+=1
		if guess in ['y','z']:
			yz+=1
	


if guess==answer: #答對時
	tries+=1
	if guess in ['a','b','c','d']:
		ad+=1
	if guess in ['e','f','g','h']:
		eh+=1
	if guess in ['i','j','k','l']:
		il+=1
	if guess in ['m','n','o','p']:
		mp+=1
	if guess in ['q','r','s','t']:
		qt+=1
	if guess in ['u','v','w','x']:
		ux+=1
	if guess in ['y','z']:
		yz+=1
	
	

	print('Congratulations! You guessed the alphabet"',answer,'" in ',tries,'tries.')
	print('Guess Histogram:')
	print("a-d:",'*'*ad)
	print("e-h:",'*'*eh)
	print("i-l:",'*'*il)
	print("m-p:",'*'*mp)
	print("q-t:",'*'*qt)
	print("u-x:",'*'*ux)
	print("y-z:",'*'*yz)