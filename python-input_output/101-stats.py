#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys


def print_stats(total_size, status_counts):
    """Prints the accumulated metrics."""
    print("File size: {:d}".format(total_size))
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    for code in valid_codes:
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


total_file_size = 0
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_counts = {code: 0 for code in valid_codes}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 2:
            try:
                file_size = int(parts[-1])
                total_file_size += file_size
            except ValueError:
                pass

            status_code = parts[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats(total_file_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_file_size, status_counts)
    raise

print_stats(total_file_size, status_counts)
