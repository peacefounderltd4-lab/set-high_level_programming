#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys


def print_metrics(total_file_size, status_codes):
    """Prints the accumulated metrics."""
    print("File size: {:d}".format(total_file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {:d}".format(key, status_codes[key]))


if __name__ == "__main__":
    total_file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                total_file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            try:
                if data[-2] in status_codes:
                    status_codes[data[-2]] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_metrics(total_file_size, status_codes)

        if line_count % 10 != 0 and line_count > 0:
            print_metrics(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_codes)
        raise
