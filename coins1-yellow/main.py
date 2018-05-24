import PuzzleHunt

def factorial(number):
	x = 1
	while number >= 1:
		x *= number
		number -= 1
	return(x)
#print(factorial(12))
  
  
  
  

#When you're ready, uncomment the code below to test:


PuzzleHunt.test_factorial(factorial)