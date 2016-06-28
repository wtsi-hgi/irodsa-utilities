# Utilities for Managing .irodsA Files
## About
This software provides a simple way to read/create the contents of the `.irodsA` files that are used by 
[iRODS](http://irods.org/). The read functionality may be useful if you have a bunch of `.irodsA` files to work with but
the associated plaintext passwords are nowhere to be found. Alternatively, the creat functionality could be helpful if 
you need to create an `.irodsA` file without having `iinit`.

The best use of these utilities however is as a reminder that `.irodsA` are not secure: they should not be left lying 
around or set with the wrong privileges!

The (arguably strange...) function that does the obfuscation is [provided in the iRODS repository]
(https://github.com/irods/irods/blob/a1db0f5defa9a34f72be3be1e4f8ae24965f9187/scripts/irods/password_obfuscation.py) - 
this script just puts a more easily usable wrapper around it.


## Prerequisites 
- Python 2.7.
- A clone of this repository. Use the `--recursive` flag to also download the iRODS submodule.


## Usage
### Unobfuscate
**Do not unobfuscate `.irodsA` files if you do not have the permission of the owner to do so!**

To unobfuscate, use the convenience script `unobfuscate.sh`. To see all options, use `--help`. 

Example using file location:
```bash
$ ./unobfuscate.sh --uid 123 example/.irodsA
examplePassword
```
Example using stdin:
```bash
$ echo ".%+90ze*M08E8(#028LED2" | ./unobfuscate.sh --uid 123 -
examplePassword
```

### Obfuscate
To obfuscate, use the convenience script `obfuscate.sh`. To see all options, use `--help`.

Example using stdin:
```bash
$ echo "examplePassword" | ./obfuscate.sh --uid 123 --mtime 123 -
.%+90ze*M08E8(#028LED2
```

Example using interactive input:
```bash
$ ./obfuscate.sh -i --uid 123
iRODS password to obfuscate:
.%+90ze*M08E8(#028LED2
```

*Note: if `uid` (a "salt") is not given, one is generated based on the value returned by Python's `os.getuid()`. The 
same `uid` is required to decode passwords.*
