import sys

try:
    assert len(sys.argv) == 2, \
        "AssertionError: more than one argument is provided"
    try:
        int(sys.argv[1])
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")

    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(e)
