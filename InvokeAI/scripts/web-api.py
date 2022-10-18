#!/usr/bin/env python3
# Copyright (c) 2022 Lincoln D. Stein (https://github.com/lstein)

import os
import re
import sys
import shlex
import copy
import warnings
import time
import traceback
sys.path.append('.')    # corrects a weird problem on Macs
from ldm.generate import Generate
g       = Generate()
outputs = g.txt2img("a unicorn in manhattan")
