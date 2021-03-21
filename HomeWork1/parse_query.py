"""This module contains functions for parsing query parameters in dictionary format."""
from urllib.parse import urlparse, parse_qsl


def parse(query: str) -> dict:
    """Returns query parameters in dictionary format"""
    parsed_url = urlparse(query)
    query_list = parse_qsl(parsed_url.query, keep_blank_values=True, encoding='utf-8')
    query_dict = {}
    for query_tuple in query_list:
        query_dict[query_tuple[0]] = query_tuple[1]
    return query_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
