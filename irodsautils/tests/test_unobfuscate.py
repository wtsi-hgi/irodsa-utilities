import os
import subprocess
import tempfile
import unittest

from irodsautils.tests._common import RUN_ENVIRONMENT, SCRIPT_DIRECTORY, OBFUSCATED_PASSWORD, PASSWORD, PYTHON_BIN, \
    UID


class TestUnobfuscate(unittest.TestCase):
    """
    Tests for un-obfuscate script.
    """
    def setUp(self):
        _, self.password_file_location = tempfile.mkstemp()
        with open(self.password_file_location, "w") as file:
            file.write(OBFUSCATED_PASSWORD)

    def tearDown(self):
        os.remove(self.password_file_location)

    def test_unobfuscate_from_file(self):
        process = subprocess.Popen(
            [PYTHON_BIN, "%s/unobfuscate.py" % SCRIPT_DIRECTORY, "--uid", str(UID), self.password_file_location],
            env=RUN_ENVIRONMENT, stdout=subprocess.PIPE)
        result = process.communicate()[0]
        self.assertEqual(result, PASSWORD)


if __name__ == "__main__":
    unittest.main()
