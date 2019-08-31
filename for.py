import sys


class my_class:
    def do_something(x):
        print("did something")


try:  # it tries and if it does not exist goes to the "except"
    x = int(sys.argv[1])
except:
    z = input("Print Number ")
    print("Z :" + str(z))

for y in range(x):  # all but the last one from the list
    print(str(y[1]))
    my_class.do_something(y)
