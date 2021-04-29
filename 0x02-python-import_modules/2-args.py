#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l > 1:
        count = 0
        if l > 2:
            print("{:d} arguments:".format(l - 1))
        else:
            print("1 argument:")
        for arg in argv:
            count += 1
            if count != 1:
                print("{:d}: {}".format(count - 1, arg))
    else:
        print("0 arguments.")
