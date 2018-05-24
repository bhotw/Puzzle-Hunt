import PuzzleHunt

def roll_snake_eyes():
  #your code goes here
  x = 0
  y = 0
  
  while (x + y) != 2:
  	x = PuzzleHunt.puzzle_randint(1,6)
  	y = PuzzleHunt.puzzle_randint(1,6)
  	
  	if (x + y) == 2:
  		print("You rolled snake eyes")
  	else:
  		print("You rolled the value",x + y)
roll_snake_eyes()
  





#When you're ready, uncomment the code below to test:

PuzzleHunt.test_roll_snake_eyes(roll_snake_eyes)