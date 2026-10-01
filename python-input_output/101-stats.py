#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys


def print_stats(total_size, status_counts):
    """Prints the accumulated metrics."""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {:d}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_file_size = 0
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_counts = {code: 0 for code in valid_codes}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            try:
                if len(parts) >= 2:
                    file_size = int(parts[-1])
                    total_file_size += file_size

                    status_code = parts[-2]
                    if status_code in status_counts:
                        status_counts[status_code] += 1
            except Exception:
                pass

            if line_count == 10:
                print_stats(total_file_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_file_size, status_counts)
        raise
        
