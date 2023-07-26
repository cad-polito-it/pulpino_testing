#!/usr/bin/env python
# Francesco Conti <f.conti@unibo.it>
#
# Copyright (C) 2016 ETH Zurich, University of Bologna.
# All rights reserved.

import sys,os,subprocess,re
import ipstools

# creates an IPApproX database
ipdb = ipstools.IPDatabase(ips_dir="./ips", skip_scripts=True)
# updates the IPs from the git repo
ipdb.update_ips()

# launch generate-ips.py
#execute("./generate-scripts.py")
