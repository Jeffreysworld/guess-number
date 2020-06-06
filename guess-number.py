import random
r = random.randint(1, 100)
while True:
	a = input('猜1個1~100的數字: ')
	a = int(a)
	if a == r:
		print('終於猜對了!')
		break
	else:
		print('猜錯了!')
		if a > r:
			print('你猜的數字比答案大')
		else:
			print('你猜的數字比答案小')
