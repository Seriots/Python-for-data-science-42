# import os  # Not allowed


def ft_tqdm(lst: range):
    """
    @Brief      Progress bar
    @Param      lst: range of values
    @Returns    None
    """

    max_size = 180
    # max_size = os.get_terminal_size().columns - 32  # Not allowed

    start = lst.start
    size = lst.stop - start

    for elem in (lst):
        use_size = max_size - len(f" {(elem - start + 1)}/{size}")
        load = int((elem - start + 1) / size * use_size) * "█"
        unload = (use_size - len(load)) * " "

        percent = (elem - start + 1) * 100 // size
        count = f"{(elem - start + 1)}/{size}"
        print(f"\r{percent:3d}%|{load}{unload}| {count}", end="")
        yield elem
