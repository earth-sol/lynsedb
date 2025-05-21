import pytest

from lynse.api.http_api.client_api import HTTPClient


def test_https_url_is_accepted():
    # Ensure that HTTPS URIs are accepted during initialization
    client = HTTPClient('https://localhost:7637', 'test_db')
    assert isinstance(client, HTTPClient)
