#!/usr/bin/python3
""" A  Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like
the following example (tabulation before -)
You must use a with statement
"""


import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    content = response.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
