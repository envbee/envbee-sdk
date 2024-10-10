# ------------------------------------
# Copyright (c) envbee
# Licensed under the MIT License.
# ------------------------------------

"""Utility classes and functions."""

from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


def add_querystring(url: str, params: dict):
    """Add query parameters to a given URL.

    This function updates the query string of a URL with the provided parameters.
    If the URL already has a query string, the parameters will be added to it.

    Args:
        url (str): The original URL to which query parameters will be added.
        params (dict): A dictionary of query parameters to add to the URL.

    Returns:
        str: The updated URL with the added query parameters.
    """
    url_parts = list(urlparse(url))

    query = dict(parse_qs(url_parts[4]))  # url_parts[4] is actual query string
    query.update(params)

    url_parts[4] = urlencode(query, doseq=True)

    return urlunparse(url_parts)