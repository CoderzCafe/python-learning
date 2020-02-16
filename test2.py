from decimal import Decimal

## global scope
x = 10


# local scope
def myfunc():
    print(x)


myfunc()


def functioninside():

    # inside funciton
    def innerfunction():
        global Y
        Y = 30
        print("X = " +str(x))

    # print the inner function to inside of the
    # function
    print(innerfunction())
    return 0


# call the functioninside()
if functioninside() is not None:
    container = functioninside()
    print("call function inside of function value(with its execution): " +str(container)+
          "\nCreated global variable value: " +str(Y))



print("0.1+0.2 = " +str(0.1+0.2))
print("round : " +str(round((0.1+0.2), 2)))

print(2.675)
print(Decimal(2.675))

print(round((Decimal(2.675)), 2))

# input with two decimal point number
y = input("input two decimal point number: ")
x = input(round((Decimal(y)), 2))

print("two decimal point number: " +str(x))
