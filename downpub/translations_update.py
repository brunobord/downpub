# -*- coding: utf-8 -*-
#!/usr/bin/env python2

import os
import sys
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'pybabel'
os.system(pybabel +
    ' extract -F babel.cfg -k lazy_gettext -o messages.pot downpub')
os.system(pybabel +
    ' update -i messages.pot -d downpub/translations')
#os.unlink('messages.pot')
