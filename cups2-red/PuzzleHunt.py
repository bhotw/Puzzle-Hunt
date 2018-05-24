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
  
def test_collatz(test_func):
  inputs = [2, 1, 100, 101, 5, 20, 15]
  outputs = [1, 4, 50, 304, 16, 10, 46]
  for i in range(len(inputs)):
    if test_func(inputs[i]) != outputs[i]:
      print("Try testing you function with parameter =", inputs[i])
      return False
  reverse_caesar_shift("VIAAIG QVWDG", 14)
  return True