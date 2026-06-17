#!/usr/bin/env python3

import sys

marker = "::::::"

for name in sys.argv[1:]:
    input = open(name, "r")
    print(marker + name)
    print(input.read())
