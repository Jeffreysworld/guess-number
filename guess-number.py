import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	a = input('猜1個1~100的數字: ')
	a = int(a)
	if a == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	else:
		print('猜錯了!')
		if a > r:
			print('你猜的數字比答案大')
		else:
			print('你猜的數字比答案小')
		print('這是你猜的第', count, '次')
