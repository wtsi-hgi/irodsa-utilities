import argparse
import sys

from irodsautils._common import read_input_using_last_argument
from irodsautils.irods.password_obfuscation import decode


def main():
    """
    Unobfuscate password entrypoint.
    """
    parser = argparse.ArgumentParser(description="De-obfuscate password from the given .irodsA file or stdin if \"-\""
                                                 "is given. Ensure you have permission to read the file")
    parser.add_argument("irodsA_file", type=str, help="Path to .irodsA file or \"-\" to use stdin")
    parser.add_argument("--uid", dest="uid", default=None, type=int,
                        help="Input to the obfuscation function, used as a salt")
    arguments = parser.parse_args()

    obfuscated = read_input_using_last_argument()
    decoded = decode(obfuscated, uid=arguments.uid)
    sys.stdout.write(decoded)


if __name__ == "__main__":
    main()
