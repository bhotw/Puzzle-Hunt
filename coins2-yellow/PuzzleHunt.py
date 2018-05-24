import io
import sys

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
        
def test_listen(func):
  inputs = [[]]
  outputs = ["Can you hear me now?Good", "Can you hear me now?Can you hear me now?Can you hear me now?Can you hear me now?Good", "Can you hear me now?"]
  sys.stdin = io.StringIO("yes\nno\norange\nyou're the worst\nyes\nstop")
  if test_func(func, inputs, outputs):
      reverse_caesar_shift("ZCCY PSVWBR VSOZHV OBR KSZZBSGG PSOA", 14)
      return True
  return False
    
    
def reverse_caesar_shift(message, shift):
  secret = ""
  message = message.upper()
  for letter in message:
    if letter == ' ':
        secret += letter
    else:
          secret += chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))
  print(secret)
