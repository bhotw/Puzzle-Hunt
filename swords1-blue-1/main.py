import PuzzleHunt

def print_greeting(hour):
  #your code goes here
 
  if 5 <= hour < 12 :
    	print( "Good morning")
  elif 12 <= hour < 16 :
    	print( "Good afternoon")
  elif 16 <= hour < 20 :
    	print( "Good evening")
  else:
  	print ("Good night")

print_greeting(16)


#When you're ready, uncomment the code below to test:

PuzzleHunt.test_print_greeting(print_greeting)