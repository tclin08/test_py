#coding=utf-8

spam=['apples',
	'bananas',
	'tofu',
	'cats']
while True:
	for i in range(0,len(spam)):
		if i != len(spam)-1:
			print(spam[i],end=''+','+' ')
		else:
			print('and',spam[i])	
	break


	

