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
