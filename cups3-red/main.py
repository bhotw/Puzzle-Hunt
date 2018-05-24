import PuzzleHunt

def repeat_collatz(number):
	x=number
	while x != 1:
		y = x % 2
		if y == 1:
			OutPut = 3 * x + 1
		else:
			OutPut = x / 2
		x = int(OutPut) 
		print(x)
repeat_collatz(3)

PuzzleHunt.test_repeat_collatz(repeat_collatz)