import sys
 
def fizzbuzz(upperbound):
    for n in range(1, upperbound):
        output = ""
        if not n % 3:
            output += "fizz"
        if not n % 5:
            output += "buzz"
        print(output or n)
 
try:
    fizzbuzz(int(sys.argv[1]))
except IndexError:
    while True:
        try:
            fizzbuzz(int(raw_input("Enter an upperbound: ")))
            break
        except:
            print("How about an integer...")
except:
    print("ERROR: The arg needs to be an integer.")