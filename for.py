import sys

try: # it tries and if it does not exist goes to the "except"
    x = int(sys.argv[1])
except:
    x = ['x','y', 'z','y']
    print("No Data")

for y in enumerate (x[:-1]):
    print (str(y[1]))

