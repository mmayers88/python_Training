<<<<<<< HEAD
import sys  # class
print(sys.argv[0])


def FizzBuzz(z):
    if (z % 3) / z == 1:
        print("Fizz")
    if (z % 2)/z < 1:
        print("buzz")
    else:
        print("this thing sucks!")


try:
    x = sys.argv[1]
    x = int(x)
    FizzBuzz(x)
except:
    x = 1
    FizzBuzz(x)
=======
import sys # importing a library
 
def fizz_buzz(z): # making a function
    if (z % 3) / z  == 1: # no need for brackets
        print("Fizz")
    if (z % 2 )/ z < 1:
        print ("Buzz")
    else : print ("Not mod 2 or 3")

try: 
    x = sys.argv[1]
    x = int (x)
    fizz_buzz(x) # calling a function

except:
    x = 1 
    fizz_buzz(x)



>>>>>>> daf59164330d81fab2f5b36b53788b6555c52a2a
