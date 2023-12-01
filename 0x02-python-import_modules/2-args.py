#!/usr/bin/python3
import sys
args_len = len(sys.argv) - 1
print("{} {}{}".format(args_len, "argument" if args_len == 1
                        else "arguments", ":" if args_len else "."))
for idx, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(idx, arg))
