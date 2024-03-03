import sys


def compute_string(string: str) -> dict:
    """
    @params:        str
    @return:        a dict with the number of occurences of each
                    character category in the string
    @description:   Take a string a count all occurences of caegory:
                    upper letter, lower letter, punctuation, digit and space
    @errors:        None
    """
    dict_out = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digits": 0
    }

    print(f"The text contains {len(string)} characters:")
    for elem in string:
        if elem.isupper():
            dict_out["upper letters"] += 1
        elif elem.islower():
            dict_out["lower letters"] += 1
        elif elem.isdigit():
            dict_out["digits"] += 1
        elif elem.isspace():
            dict_out["spaces"] += 1
        else:
            dict_out["punctuation marks"] += 1
    return dict_out


def main():
    """
    @description:   Check if the number of arguments is correct
                    and call the compute_string function,
                    if no arguments are given, prompt the user to give a string
    @errors:        If more than one argument is given, raise an AssertionError
    @return:        None
    """
    try:
        assert len(sys.argv) <= 2, \
            "AssertionError: more than one argument is provided"
    except AssertionError as e:
        print(e)
        return

    result_dict = {}
    if len(sys.argv) == 1:
        # keep carriage return
        print("What is the text to count?")
        s = sys.stdin.readline()
        result_dict = compute_string(s)
    else:
        result_dict = compute_string(sys.argv[1])

    [print(i[1], i[0]) for i in result_dict.items()]


if __name__ == "__main__":
    main()
