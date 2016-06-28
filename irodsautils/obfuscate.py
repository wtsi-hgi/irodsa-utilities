import argparse
from sys import stdin, stdout
from getpass import getpass

from irodsautils._common import read_input_using_last_argument
from irodsautils.irods.password_obfuscation import encode


def main():
    """
    Obfuscate password entrypoint.
    """
    parser = argparse.ArgumentParser(description="Obfuscates a password in the same way as iRODS passed in via stdin "
                                                 "or interactively")
    parser.add_argument("-i", dest="interactive", action="store_true", help="Interactively input password")
    parser.add_argument("--uid", dest="uid", default=None, type=int,
                        help="Input to the obfuscation function, used as some kind of salt")
    parser.add_argument("--mtime", dest="mtime", default=None, type=int,
                        help="Some other input to the obfuscation function that might be a salt or may also be "
                             "extractable from the obfuscated result")
    parser.add_argument("password_file", nargs="?", type=str, default=None,
                        help="Path to file containing password or \"-\" to use stdin")
    arguments = parser.parse_args()

    if arguments.interactive:
        password = getpass(prompt="iRODS password to obfuscate:")
    elif arguments.password_file is None:
        raise ValueError("Either password file location must be given (\"-\" for stdin) or used interactively with -i")
    else:
        password = read_input_using_last_argument()

    encoded = encode(password, uid=arguments.uid, mtime=arguments.mtime).split("\x00")[0]
    stdout.write(encoded)


if __name__ == "__main__":
    main()
