that reads stdin line by line and computes metrics.
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
