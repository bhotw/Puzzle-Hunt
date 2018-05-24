#import PuzzleHunt

def repeat_collatz_with_count(number):
	x=number
	c = 0
	while x != 1:
		c += 1
		y = x % 2
		if y == 1:
			OutPut = 3 * x + 1
		else:
			OutPut = x / 2
		x = int(OutPut) 
		print(c,":",x)
repeat_collatz_with_count(1709174063824403857145856)

