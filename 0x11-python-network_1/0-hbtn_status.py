#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""
if __name__ == '__main__':
        import urllib.request
            with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
                        content = res.read()
                                print("Body response:")
                                        print("\t- type: {}".format(type(content)))
                                                print("\t- content: {}".format(content))
                                                        print("\t- utf8 content: {}".format(content.decode('utf-8')))#!/usr/bin/python3
"""Fetches the URL: https://intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen
if __name__ == "__main__":
    req = Request('https://intranet.hbtn.io/status')
    with urlopen(req) as res:
        content = res.read()
        utf8_content = content.decode('utf-8')
        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(content)))
        print('\t- content: {_content}'.format(_content=content))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=utf8_content))
