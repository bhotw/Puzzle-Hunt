import PuzzleHunt

def roll_die():
  x = PuzzleHunt.puzzle_randint(1,6)
  print("You rolled the value",x)
roll_die()


  
#When you're ready, uncomment the code below to test:

PuzzleHunt.test_roll_die(roll_die)