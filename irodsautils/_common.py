import fileinput

import sys


def read_input_using_last_argument():
    """
    Reads input from the location specified by the last argument given in the program call.

    Not thread-safe if reading arguments in parallel.
    :return:
    """
    assert len(sys.argv) >= 2
    original_arguments = sys.argv[:]
    # Note: rebinding `sys.argv` does not work
    while sys.argv[1] != sys.argv[-1]:
        sys.argv.pop(1)
    input = fileinput.input().readline()
    # Restore `sys.argv`
    while len(original_arguments) > 2:
        sys.argv.insert(len(sys.argv) - 1, original_arguments.pop(1))
    return input