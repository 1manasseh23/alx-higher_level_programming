#!/usr/bin/python3

import sys

total_file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        data = line.split()
        total_file_size += int(data[-1])
        status_code = data[-2]
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


"""
import sys

def print_metrics():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401 0, 403: 0, 404: 0, 405: 0,  500: 0}
    count = 0

    for line in sys.stdin:
        count += 1
        split_line = line.split()
        try:
            size = int(split_line[-1])
            total_size += size
        except:
            pass
        try:
            status_code = int(split_line[-2])
            if status_code in status_codes:
                status_codes[status_code] + 1
        except:
            pass

        if count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))

    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
"""
