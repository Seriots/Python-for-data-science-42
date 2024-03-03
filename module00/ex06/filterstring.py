import sys

from ft_filter import ft_filter


def main():
    """
    @Brief      Main function
    @Param      sys.argv: list of arguments, one string and one integer
    @Raises     AssertionError: if the number of arguments is not 2
                or if types are not correct
    @Desc       Print all characters of the string
                that are longer than the second argument
    @Returns    None
    """
    try:
        assert len(sys.argv) == 3, \
            "AssertionError: the arguments are bad"
        assert sys.argv[2].isdigit(), \
            "AssertionError: the arguments are bad"
    except AssertionError as e:
        print(e)
        return

    ft = ft_filter(lambda x: len(x) > int(sys.argv[2]), sys.argv[1].split())
    result = [i for i in ft]
    print(result)


if __name__ == "__main__":
    main()
