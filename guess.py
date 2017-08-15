import random

guess = random.randint(1,20)

for i in range(6): 
	print('input guess  No   ')
	in_guess = input()
	in_guess = int (in_guess)
	if in_guess < guess:
		print('your No is low')
	elif in_guess > guess:
		print('your No is big')
	else:
		print('right')
		break

