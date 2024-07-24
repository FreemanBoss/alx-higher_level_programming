#!/usr/bin//python3
"""Take a URL, send request and display X-Request-Id"""
import sys
import urllib.request


url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
except Exception as e:
    print(e)
