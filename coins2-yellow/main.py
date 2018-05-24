import PuzzleHunt

def listen():
  #your code goes here
  inpt = "no"
  while inpt != "stop":
  	inpt = input("Can you hear me now?")
  	if inpt == "yes":
  		print("Good")

  
  
  
#When you're ready, uncomment the code below to test:

PuzzleHunt.test_listen(listen) 