import argparse
import fileinput

import sys

from irodsautils.irods.password_obfuscation import decode


def main():
    """
    Unobfuscate password entrypoint.
    """
    parser = argparse.ArgumentParser(description="De-obfuscate password from the given .irodsA file or stdin if \"-\""
                                                 "is given. Ensure you have permission to read the file")
    parser.add_argument("irodsA_file_location", type=str, help="Path to .irodsA file or \"-\" to use stdin")
    parser.add_argument("--uid", dest="uid", default=None, type=int,
                        help="Input to the obfuscation function, used as a salt")
    arguments = parser.parse_args()

    if arguments.uid is not None:
        # Hack to stop `fileinput` from thinking the value of "--uid" is the file location
        if "=" not in sys.argv[1]:
            del sys.argv[2]
        del sys.argv[1]

    obfuscated = fileinput.input().readline()
    decoded = decode(obfuscated, uid=arguments.uid)
    sys.stdout.write(decoded)


if __name__ == "__main__":
    main()
