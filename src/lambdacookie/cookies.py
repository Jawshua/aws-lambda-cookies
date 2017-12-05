import sys
import string
from lambdacookie.caseiter import case_iteration

if sys.version_info >= (3, 0):
    import http.cookies as cookielib
    string_type = str
else:
    import Cookie as cookielib
    string_type = basestring


def headers(lst, header="set-cookie"):
    """
    Processes a list of cookies and returns a dict of MIME
    header names to values. A case varied version of the header param is used
    as the key for each entry in the returned dict.

    Keyword arguments:
    lst       -- A list of cookies to output. List items may be strings or
                 instances of BaseCookie.
    header    -- the name of the HTTP header used to set cookies
                 (default: 'Set-Cookie')
    """

    if not isinstance(lst, list):
        raise TypeError('Expected a list of string or BaseCookie')

    result = {}

    for i, item in enumerate(lst):
        if isinstance(item, string_type):
            item = cookielib.SimpleCookie(item)
        elif not isinstance(item, cookielib.BaseCookie):
            raise TypeError('Expected a list of string or BaseCookie')

        header = case_iteration(header, i)
        result[header] = item.output(header='')[1:]

    return result
