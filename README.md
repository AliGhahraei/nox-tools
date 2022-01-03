# nox-tools
## Predefined sessions for [nox](https://github.com/theacodes/nox)

To use these sessions, just install nox-tools and import them in your
noxfile.py. You can also configure their behavior by setting the config object's
attributes.

``` python
from nox_tools import tests, typing

config.module = 'my_module_name'
```

You can find out how to use each session and the config object by reading the
[docstrings](nox_tools/sessions.py)
