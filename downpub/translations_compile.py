# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import os
import sys
if sys.platform == 'win32':
    pybabel = 'flask\\Scripts\\pybabel'
else:
    pybabel = 'pybabel'
os.system(pybabel + ' compile -f -d downpub/translations')