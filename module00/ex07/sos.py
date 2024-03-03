import sys


def main():
    """
    @Brief      Main function
    @Param      sys.argv: list of arguments, one string
    @Raises     AssertionError: if the number of arguments is not 2
    @Desc       Print the morse code of the string
    @Returns    None
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    try:
        assert len(sys.argv) == 2, \
            "AssertionError: the arguments are bad"
        for i in sys.argv[1]:
            assert i.isalnum() or i.isspace(), \
                "AssertionError: the arguments are bad"
    except AssertionError as e:
        print(e)
        return

    for i in sys.argv[1].upper():
        print(NESTED_MORSE[i], end="")
    print()


if __name__ == "__main__":
    main()
