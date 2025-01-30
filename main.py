#!/usr/bin/python3

import os
import sys
from file_manager import FileManager

print("Hello md-to-any")

if os.path.isdir(sys.argv[1]):
    print("Vault: ", sys.argv[1])



vault = sys.argv[1]

file_mgr = FileManager(sys.argv[1])
