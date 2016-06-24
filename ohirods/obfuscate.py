import argparse
from getpass import getpass

from ohirods.irods.password_obfuscation import encode


def main():
    """
    Obfuscate password entrypoint.
    """
    parser = argparse.ArgumentParser(description="Obfuscates a password in the same way as iRODS. A password is to be "
                                                 "entered when the program starts.")
    parser.parse_args()
    password = getpass(prompt="iRODS password to obfuscate:")
    encoded = encode(password)
    print(encoded)


if __name__ == "__main__":
    main()
