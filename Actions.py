import time
import random
import os

mode = input("choose update frequency ('slow', 'medium', 'fast', 'fastest'): ")

if mode == "slow":
	barrier = 1.0
elif mode == "medium":
	barrier = 0.5
elif mode == "fast":
	barrier = 0.10
elif mode == "fastest":
	barrier = 0.05
else:
	barrier = 0.5

brackets = ''
while True:
	a = random.randint(0, 1)
	if len(brackets) <= 100:
		brackets += '(' if a else ')'
	else:
		brackets = brackets[1:] + '(' if a else brackets[1:] + ')'

	heights = []
	height = 0
	min_height = 0
	max_height = 0

	for i in range(len(brackets)):
		if i == 0:
			heights.append(height)
			continue

		if brackets[i] == brackets[i - 1]:
			if brackets[i] == ')':
				height -= 1
				if height < min_height:
					min_height = height
			else:
				height += 1
				if height > max_height:
					max_height = height
		else:
			heights.append(heights[i - 1])
			continue

		heights.append(height)

	for i in range(len(brackets)):
		if min_height < 0:
			heights[i] += abs(min_height)

	for i in range(max_height - min_height, -1, -1):  # output
		for j in range(len(brackets)):
			if heights[j] == i:
				if brackets[j] == '(':
					print('/', end='')
				else:
					print('\\', end='')
			else:
				print(' ', end='')
		print()
	timer = time.time()
	while time.time() - timer < barrier:
		continue
	os.system('cls')
	print("stocks rating of SD-company:")
