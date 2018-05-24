import PuzzleHunt

def roll_dice():
  x = PuzzleHunt.puzzle_randint(1,6)
  y = PuzzleHunt.puzzle_randint(1,6)
  print("You rolled the value",x + y)
roll_dice()

  



  
#When you're ready, uncomment the code below to test:

PuzzleHunt.test_roll_dice(roll_dice)