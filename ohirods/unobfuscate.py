import argparse
from ohirods.irods.password_obfuscation import decode


def main():
    """
    Unobfuscate password entrypoint.
    """
    irods_a_file_location = get_input_file_location()
    obfuscated = get_obfuscated_password(irods_a_file_location)
    decoded = decode(obfuscated)
    print(decoded)


def get_input_file_location():
    """
    Gets the input .irodsA file path location from the program arguments.
    :return: the location of the .irodsA file
    """
    parser = argparse.ArgumentParser(description="De-obfuscate password from the given .irodsA file (you MUST have "
                                                 "permission to read this password file from its owner).")
    parser.add_argument("irodsA_file_location", type=str, help="Path to .irodsA file to de-obfuscate password from")
    arguments = parser.parse_args()
    return arguments.irodsA_file_location


def get_obfuscated_password(irods_a_file_location):
    """
    Gets the obfuscated password from .irodsA file in the given location.
    :param irods_a_file_location: the location of the .irodsA file
    :return: the obfuscated password
    """
    with open(irods_a_file_location, "r") as file:
        return file.read()


if __name__ == "__main__":
    main()
