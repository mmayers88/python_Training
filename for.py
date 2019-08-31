import sys
class my_class:
    def do_something(x):
        print("did something")

try:
    x = int(sys.argv[1])
except:
    x = ['x','y','z','y']
    print("No Data")

for y in enumerate(x[:-1]):
    print(str(y[1]))
    my_class.do_something(y)


