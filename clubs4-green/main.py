import PuzzleHunt

def play_game(jellybean_count):
  #your code goes here
  print("Starting amount:",jellybean_count)
  while jellybean_count >= 0:
  	x= PuzzleHunt.puzzle_randint (1,6)
  	y= PuzzleHunt.puzzle_randint (1,6)
  	z= x+y
  	print("You rolled the value", z)
  	if z == 7:
  		jellybean_count += 1
  	elif z == 11:
  		jellybean_count += 2
  	elif z == 3 or z == 5 or z == 9:
  		jellybean_count -= 2
  	elif z == 2:
  		jellybean_count -= 4
  	if jellybean_count < 0:
  		print("You're out of jellybeans")
  	else:
  		print("Jellybeans remaining:", jellybean_count)
play_game(15)