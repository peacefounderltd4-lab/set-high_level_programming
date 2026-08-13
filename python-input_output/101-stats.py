#!/usr/bin/python3
"""Read stdin and compute metrics."""


import sys


def print_stats(size, status_codes):
    """Print file size and status code statistics."""
    print("File size: {}".format(size))

    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


size = 0
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

        if len(parts) >= 7:
            try:
                file_size = int(parts[-1])
                status = int(parts[-2])
            except ValueError:
                continue

            size += file_size

            if status in status_codes:
                status_codes[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats(size, status_codes)

except KeyboardInterrupt:
    pass

print_stats(size, status_codes)
