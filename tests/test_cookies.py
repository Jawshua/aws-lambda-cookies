import pytest
from lambdacookie.cookies import *
if sys.version_info >= (3, 0):
    import http.cookies as cookielib
else:
    import Cookie as cookielib


def test_headers_str():
    assert headers(["a=b"]) == {"set-cookie": "a=b"}


def test_headers_cookie():
    cookie = cookielib.BaseCookie('a=b; domain=.example.com')
    assert headers([cookie]) == {"set-cookie": "a=b; Domain=.example.com"}


def test_headers_type_exception():
    with pytest.raises(TypeError):
        assert headers('str')

    with pytest.raises(TypeError):
        assert headers([None])


def test_headers_custom_header():
    assert headers(["a=b"], "cookie") == {"cookie": "a=b"}

