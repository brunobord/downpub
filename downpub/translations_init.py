# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import sys
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'pybabel'
if len(sys.argv) != 2:
    print("usage: tr_init <language-code>")
    sys.exit(1)
os.system(pybabel +
    ' extract -F babel.cfg -k lazy_gettext -o messages.pot downpub')
os.system(pybabel
    + ' init -i messages.pot -d downpub/locales -l ' + sys.argv[1])
os.unlink('messages.pot')