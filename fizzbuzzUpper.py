import sys


print "The name of this script is {}.".format(sys.argv[0])


# Case where user supplied the upper value when calling the script (eg. "python fizzbuzzUpper.py 100")
# Use sys.argv[1] to capture the supplied input
# Exception to handle non-integer upper value using raw_input() for user to retry input
if len(sys.argv) == 2:
  try:
    n = int(sys.argv[1])
    print "User supplied {} as the upper value for the game.".format(n)
  except ValueError:
    while True:
      try:
        n = int(raw_input("Please enter only one integer number for the upper value of the game: "))
        break
      except:
        print "How about just an integer?"
        
# Case where user does not supply the upper value when calling the script (eg. "python fizzbuzzUpper.py")
# Use raw_input() for user to supply the upper value
# Exception to handle non-integer upper value using raw_input() for user to retry input
elif len(sys.argv) == 1:
  try:
    n = int(raw_input("Enter an upper value for the FizzBuzz game: "))
  except ValueError:
    while True:
      try:
        n = int(raw_input("Please enter only one integer number for the upper value of the game: "))
        break
      except:
        print "How about just an integer?"

# Case where user supplies more than one value when calling the script (eg. "python fizzbuzzUpper.py 50 100)
# Exception to handle non-integer upper value using raw_input() for user to retry input
else:
  try:
    n = int(raw_input("Please enter only one integer number for the upper value of the game: "))
  except ValueError:
    while True:
      try:
        n = int(raw_input("Please enter only one integer number for the upper value of the game: "))
        break
      except:
        print "How about just an integer?"

        
print "FizzBuzz counting up to {}.".format(n)


for i in range(1, (n + 1)):
  if i % 3 == 0 and i % 5 == 0:
    print "FizzBuzz"
  elif i % 5 == 0:
    print "Buzz"
  elif i % 3 == 0:
    print "Fizz"
  else:
    print i