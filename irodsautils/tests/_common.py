import os

PROJECT_ROOT = os.path.join("..", "..")
RUN_ENVIRONMENT = dict(os.environ, PYTHONPATH=PROJECT_ROOT)
SCRIPT_DIRECTORY = os.path.join("..")
PASSWORD = "test"
OBFUSCATED_PASSWORD = ".%+90ze93IF"
UID = 123
MTIME = 123
PYTHON_BIN = "python2"