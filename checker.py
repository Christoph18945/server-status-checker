#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""check website connectivity"""

import argparse
from httplib2 import Response
import requests

def main() -> None:
    """main function"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Check connectivity to a given URL.")
    parser.add_argument("url", help="URL to check connectivity.")
    args: argparse.Namespace = parser.parse_args()
    # call to check connectivity
    if isinstance(args.url, str):
        check_server_connectivity(args.url)
    else:
        print(f"{args.url} is no string!")

def check_server_connectivity(url: str) -> None:
    """Check connection to URL."""
    try:
        reply: Response = requests.get(url, timeout=5)
        reply.raise_for_status()
        print(f"Connected to {url} successfully. Status code: {reply.status_code}")
    except requests.RequestException as e:
        # print message if exception occurs
        print(f"Failed to connect to {url}. Error: {e}")

if __name__ == "__main__":
    main()
