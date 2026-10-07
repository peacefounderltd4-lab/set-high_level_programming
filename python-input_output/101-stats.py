#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys


def print_stats(size, status_codes):
    """Print the accumulated statistics.

    Args:
        size (int): Total file size calculated so far.
        status_codes (dict): Dictionary mapping status code to count.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            tokens = line.split()

            try:
                total_size += int(tokens[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = tokens[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
￼Enter
