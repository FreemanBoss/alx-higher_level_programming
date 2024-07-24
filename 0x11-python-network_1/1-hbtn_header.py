#!/usr/bin//python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import sys
import urllib.request


url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
except Exception as e:
    print(e)
