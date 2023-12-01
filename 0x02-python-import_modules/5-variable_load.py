#!/usr/bin/python3

import importlib.util
import sys

def load_variable_value(file_path):
    spec = importlib.util.spec_from_file_location("variable_load_5", file_path)

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    print(module.a)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <file_path>".format(sys.argv[0]))
        sys.exit(1)

    file_path = sys.argv[1]
    load_variable_value(file_path)
