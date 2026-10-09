#!/usr/bin/python3
"""Parse log lines and compute metrics."""
import sys


def print_stats(total_size, status_codes):
    """Print the accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Read stdin and compute log metrics."""
    total_size = 0
    status_codes = {}
    line_count = 0
    valid_codes = [
        '200', '301', '400', '401',
        '403', '404', '405', '500'
    ]

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) < 9:
                continue

            try:
                status = parts[-2]
                size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            total_size += size

            if status in valid_codes:
                status_codes[status] = (
                    status_codes.get(status, 0) + 1
                )

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
