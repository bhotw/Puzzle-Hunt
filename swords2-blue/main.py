import PuzzleHunt
x = 1 
while x <= 750:
	y = x % 7 
	if  y == 0:
		PuzzleHunt.get_secret_letter(x)
		
	x = x + 1