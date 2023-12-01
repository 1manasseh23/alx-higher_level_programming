#!/usr/bin/python3.8

import dis
import importlib.util
import sys

def print_hidden_names(file_path):
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    module_attributes = dir(module)

    for name in sorted(module_attributes):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <compiled_module_path>".format(sys.argv[0]))
        sys.exit(1)

    compiled_module_path = sys.argv[1]
    print_hidden_names(compiled_module_path)
