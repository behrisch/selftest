#!/usr/bin/env python

import os, sys

def generateFile(name, sec):
    print >>file(name, "w"), sec

if len(sys.argv) == 1:
    generateFile(os.path.join(os.getenv("TEXTTEST_LOG_DIR"), "partial1_time"), "3")
    generateFile(os.path.join(os.getenv("TEXTTEST_LOG_DIR"), "partial2_time"), "5")
