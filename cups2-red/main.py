import PuzzleHunt
def collatz(number):
	x = number
	y = x % 2
	if y == 1:
	  OutPut = 3 * x + 1
	else:
	  OutPut = x / 2
	return OutPut

PuzzleHunt.test_collatz(collatz) 