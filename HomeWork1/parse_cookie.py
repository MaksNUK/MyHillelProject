"""This module contains functions for parsing cookies in dictionary format."""
from http.cookies import SimpleCookie


def parse_cookie(query: str) -> dict:
    """Returns cookie parameters in dictionary format"""
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
