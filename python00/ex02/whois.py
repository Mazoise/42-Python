import sys


try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) == 2:
        assert sys.argv[1].isdigit(), "argument is not integer"
        res = int(sys.argv[1])
        if res == 0:
            print("I'm Zero.")
        elif res % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as e:
    print("AssertionError: %s" % e)
