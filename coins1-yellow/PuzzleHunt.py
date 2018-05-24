def reverse_caesar_shift(message, shift):
  secret = ""
  message = message.upper()
  for letter in message:
      if letter == ' ':
          secret += letter
      else:
          secret += chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))
  print(secret)
  return True 
  
def test_factorial(test_func):
  inputs = [1, 2, 5, 6, 8, 10, 12]
  outputs = [1, 2, 120, 720, 40320, 3628800, 479001600]
  for i in range(len(inputs)):
    if test_func(inputs[i]) != outputs[i]:
      print("Try testing you function with parameter =", inputs[i])
      return False
  for i in range(38):
    print(i and"|"+["-"*57,(" *  "*7)[i%2*2:][:(i<11)*23].ljust(56,"  #"[i%3])+"|"][1<i<21]*(i<22))
  return True