import random

random_nums = [39, 28, 485, 230, 103, 23, 103, 4, 20, 342, 934, 3490, 42, 90, 40, 394, 2827, 10, 6, 5, 1, 1, 5, 4, 1, 2, 6, 5, 30, 3234, 34, 765, 674, 458]
rand_index = 0
testing = False

import sys
import io

class Capturing(list):
  def __enter__(self):
      self._stdout = sys.stdout
      sys.stdout = self._stringio = io.StringIO()
      return self
  def __exit__(self, *args):
      self.extend(self._stringio.getvalue().splitlines())
      del self._stringio    # free up some memory
      sys.stdout = self._stdout

def test_func(func, inputs, real_output):
  test_output = []
  with Capturing() as test_output:
      for param in inputs:
          func(*param)
  if len(real_output) != len(test_output):
      if len(inputs) == 0:
          print("Try testing your function!")
      else:
          print("Try testing your function with various inputs")
      return False
  for i in range(len(real_output)):
      if real_output[i] != test_output[i]:
          if len(inputs) > i or len(inputs) == 0:
              print("Try testing your function!")
          else:
              print("Try testing your function with parameter =", inputs[i])
          return False
  return True
            
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

def puzzle_randint(min_num, max_num):
    global testing
    if testing:
        diff = max_num - min_num + 1
        global rand_nums 
        global rand_index
        rand_num = (random_nums[rand_index] % diff) + min_num
        rand_index = (rand_index + 1) % len(random_nums)
        return rand_num
    else:
        return random.randint(1,6)

def test_roll_snake_eyes(func):
    global testing
    global rand_index
    testing = True
    rand_index = 0
    inputs = [[]]
    outputs = ["You rolled the value 9", "You rolled the value 9", "You rolled the value 8", "You rolled the value 7",
                "You rolled the value 4", "You rolled the value 10", "You rolled snake eyes"]
    success = test_func(func, inputs, outputs)
    if success:
        reverse_caesar_shift("CIHGWRS XODOB", 14)
    testing = False
    return success