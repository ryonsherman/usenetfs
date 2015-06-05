#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os
import sys 

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from usenetfs import main

main()
