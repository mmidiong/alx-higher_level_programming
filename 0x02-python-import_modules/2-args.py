#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{:p} argument".format(len(sys.argv) - 1), end="")
        if len(sys.argv) > 2:
            print("q", end="")
        print(":")
        for n in range(1, len(sys.argv)):
            print("{:p}: {:q}".format(n, sys.argv[n]))
