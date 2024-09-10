---
tags:
  - venting
  - yak-shaving
  - posts
date: 2024-07-15
---
When Poetry lists the dependencies for a package it doesn't show the Python versions that those ranges are valid for.  For example, [this](https://github.com/boto/botocore/blob/develop/setup.py) `setup.py`:

```python
requires = [
    'jmespath>=0.7.1,<2.0.0',
    'python-dateutil>=2.1,<3.0.0',
    # Prior to Python 3.10, Python doesn't require openssl 1.1.1
    # but urllib3 2.0+ does. This means all botocore users will be
    # broken by default on Amazon Linux 2 and AWS Lambda without this pin.
    'urllib3>=1.25.4,<1.27 ; python_version < "3.10"',
    'urllib3>=1.25.4,!=2.2.0,<3 ; python_version >= "3.10"',
]
```

will not have the Python version shown when running `poetry show`, despite some the package ranges depending on the Python version of the project.  On a Python project where the `pyproject.toml` specifies Python 3.9, `poetry show` will only return the urllib3 version range that is valid for Python 3.9.

```bash
[~/projects/prosebit] (develop)  
> head pyproject.toml
[tool.poetry]
name = "prosebit"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "3.9"

[~/projects/prosebit] (develop)  
> poetry show botocore
 name         : botocore                               
 version      : 1.34.144                               
 description  : Low-level, data-driven core of boto 3. 

dependencies
 - jmespath >=0.7.1,<2.0.0
 - python-dateutil >=2.1,<3.0.0
 - urllib3 >=1.25.4,<1.27

required by
 - boto3 >=1.34.144,<1.35.0
 - s3transfer >=1.33.2,<2.0a.0
```

 On a Python project where the `pyproject.toml` specifies Python 3.10, `poetry show` will only return the urllib3 version range that is valid for Python 3.10.

```bash
[~/projects/prosebit] (develop)  
> head pyproject.toml
[tool.poetry]
name = "prosebit"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "3.10"

[~/projects/prosebit] (develop)  
> poetry show botocore
 name         : botocore                               
 version      : 1.34.144                               
 description  : Low-level, data-driven core of boto 3. 

dependencies
 - jmespath >=0.7.1,<2.0.0
 - python-dateutil >=2.1,<3.0.0
 - urllib3 >=1.25.4,<2.2.0 || >2.2.0,<3

required by
 - boto3 >=1.34.144,<1.35.0
 - s3transfer >=1.33.2,<2.0a.0
```

On a Python project where a range is specified that covers multiple urllib3 package ranges, **`poetry show` will show both ranges without specifying that the ranges apply to different Python versions**.

```bash
[~/projects/prosebit] (develop)  
> head pyproject.toml
[tool.poetry]
name = "prosebit"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = ">=3.9,<3.12"

[~/projects/prosebit] (develop)  
> poetry show botocore
 name         : botocore                               
 version      : 1.34.144                               
 description  : Low-level, data-driven core of boto 3. 

dependencies
 - jmespath >=0.7.1,<2.0.0
 - python-dateutil >=2.1,<3.0.0
 - urllib3 >=1.25.4,<1.27
 - urllib3 >=1.25.4,<2.2.0 || >2.2.0,<3

required by
 - boto3 >=1.34.144,<1.35.0
 - s3transfer >=1.33.2,<2.0a.0
```

Despite displaying both ranges in `poetry show`, **Poetry will only use the oldest range when running `poetry lock` or `poetry install`** .  This can lead to a disconnect between the package ranges that Poetry is reporting as valid and the package ranges that Poetry will actually attempt to use when running.

I discovered this the hard way when trying to install `kinde-python-sdk` and `boto3` within the same project. `boto3` requires `botocore` which requires `urllib3`.  `kinde-python-sdk` also requires `urllib3`. Since my project was set to use `python = ">=3.9,<3.12"`, Poetry was listing both ranges in `poetry show`, but only using the range `urllib3 >=1.25.4,<1.27` when installing `botocore`. This resulted in headaches because `kinde-python-sdk` requires `urllib3 >=2.2.1,<2.3.0`, so it appeared like `botocore` and `kinde-python-sdk` could coexist when I ran `poetry show`, but failed to install every time I tried.

Another important detail to note is that **this is all dependent on the Python version specified in `pyproject.toml`.  The Python version you are actually running does not change the behaviour of Poetry.**  I ran into all of these problems when running Python 3.11, so was confused for hours.

`poetry show` should report the Python versions that each package dependency range is valid for, since this turned a relatively simple dependency conflict into a multi-hour dependency conflict.  I was only able to figure out the exact cause by reading the setup script for `botocore`.