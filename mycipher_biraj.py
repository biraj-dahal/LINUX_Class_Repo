# get the shift argument from the CLI
import sys
shift_value = int(sys.argv[1])

result = "" # holder for encoded w/o formatting

# if you are taking input from stdin to record encoded w/o formatting
for line in sys.stdin:
  for letter in line.upper():
    if letter.isalpha():
      result += chr((ord(letter) + shift_value)) if (ord(letter)+shift_value) <= ord('Z') else chr((ord(letter) + shift_value - 26))

""" 
/*--*/if you are trying to access with a file to record encoded w/o formatting
with open('plaintext', 'r') as f:
  helper_string = f.read().upper()
for letter in helper_string:
  if letter.isalpha():
    result += chr((ord(letter) + shift_value)) if (ord(letter)+shift_value) <= ord('Z') else chr((ord(letter) + shift_value - 26))
"""

# print encoded data with formatting
letters_count=1
for i in result:
  if letters_count % 5 != 0:
    print(i, end ="")
  elif letters_count % 50 == 0:
    print(i, end = " \n")
  else:
    print(i, end = " ")
  letters_count+=1
print("\n")
  