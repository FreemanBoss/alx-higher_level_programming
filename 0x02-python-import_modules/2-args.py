#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    #count = len(sys.argv) - 1
    argument = sys.argv[1:]
    count = len(argument)
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        #print("{}: {}".format(i + 1, sys.argv[i + 1]))
        print(str(i + 1) + ": " + argument[i])
