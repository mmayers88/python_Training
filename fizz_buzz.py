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



