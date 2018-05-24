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
  
def test_is_even(test_func):
  inputs = [2, 1, 100, 101, 0, -16, -15]
  outputs = [True, False, True, False, True, True, False]
  for i in range(len(inputs)):
    if test_func(inputs[i]) != outputs[i]:
      print("Try testing you function with parameter =", inputs[i])
      return False
  reverse_caesar_shift("ZCCY PSVWBR HVS QSFSOZ", 14)
  return True
  
