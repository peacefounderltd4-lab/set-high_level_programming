#!/usr/bin/python3
"""Read stdin and compute metrics."""

import sys


def print_stats(total_size, status_codes):
    """Print accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 2:
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except ValueError:
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
                continue

            total_size += size
            if status in status_codes:
                status_codes[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    pass

print_stats(total_size, status_codes)
