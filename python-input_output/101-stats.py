#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
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

counter = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            status = int(parts[-2])
            file_size = int(parts[-1])

            if status in status_codes:
                status_codes[status] += 1

            total_size += file_size
        except (ValueError, IndexError):
            pass

        counter += 1
        if counter % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_codes)
