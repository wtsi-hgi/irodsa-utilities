# Utilities for Managing .irodsA Files
*Do not unobfuscate `.irodsA` files where you do not have the permission of the owner to do so!*

## About
This software provides a simple way to read/write the contents of `.irodsA` files, used by [iRODS](http://irods.org/). 
The (arguably strange...) function that does the obfuscation is [provided in the iRODS repository]
(https://github.com/irods/irods/blob/a1db0f5defa9a34f72be3be1e4f8ae24965f9187/scripts/irods/password_obfuscation.py) 
- this script merely puts a more easily usable wrapper around it.

## Usage
### Unobfuscate
To unobfuscate, use the convenience script `unobfuscate.sh`. To see all options, use `--help`.

Example via file location:
```bash
$ ./unobfuscate.sh --uid 123 example/.irodsA
examplePassword
```
Example via stdin:
```bash
$ echo ".%+90ze*M08E8(#028LED2" | ./unobfuscate.sh --uid 123 -
examplePassword
```


### Obfuscate
To obfuscate, use the convenience script `obfuscate.sh`. To see all options, use `--help`.

Example:
```bash
$ echo "examplePassword" | ./obfuscate.sh --uid 123 --mtime 123
.%+90ze*M08E8(#028LED2
```
