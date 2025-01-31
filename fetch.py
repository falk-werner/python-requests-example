#!/usr/bin/env python3

import requests
import argparse
from sys import stderr

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, nargs=1)
    args = parser.parse_args()
    response = requests.get(args.url[0])
    if not response.ok:
        print(f"error: status={response.status_code}", file=stderr)
        exit(1)
    print(response.text)

if __name__ == "__main__":
    main()

