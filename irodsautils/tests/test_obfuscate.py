import os
import subprocess
import tempfile
import unittest

from irodsautils.tests._common import RUN_ENVIRONMENT, SCRIPT_DIRECTORY, OBFUSCATED_PASSWORD, PASSWORD, PYTHON_BIN, \
    UID, MTIME


class TestObfuscate(unittest.TestCase):
    """
    Tests for obfuscate script.
    """
    def setUp(self):
        _, self.password_file_location = tempfile.mkstemp()
        with open(self.password_file_location, "w") as file:
            file.write(PASSWORD)

    def tearDown(self):
        os.remove(self.password_file_location)

    def test_obfuscate_from_file(self):
        process = subprocess.Popen(
            [PYTHON_BIN, "%s/obfuscate.py" % SCRIPT_DIRECTORY, "--uid", str(UID), "--mtime", str(MTIME)],
            env=RUN_ENVIRONMENT, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        result = process.communicate(PASSWORD)[0]
        self.assertEqual(result, OBFUSCATED_PASSWORD)


if __name__ == "__main__":
    unittest.main()
