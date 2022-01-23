# nox-tools
## Predefined sessions for [nox](https://github.com/theacodes/nox)

To use these sessions, just install nox-tools, import them in your noxfile.py
and either set config.sessions to a list with the ones you want or manually 
mark each one as a session using nox.session. You can also configure their
behavior by setting the config object's attributes.

``` python
from nox_tools import config, tests, typing

config.module = 'my_module_name'
config.sessions = [tests, typing]
```

You can find out how to use each session and the config object by reading the
[docstrings](nox_tools/sessions.py)
