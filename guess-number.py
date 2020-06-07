import random
start = input('請輸入隨機數字開始值: ')
end = input('請輸入隨機數字結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	a = input('猜1個數字: ')
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
