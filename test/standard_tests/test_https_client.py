import pytest

from lynse.api.http_api.client_api import HTTPClient


def test_https_url_is_accepted():
    # Ensure that HTTPS URIs are accepted during initialization
    client = HTTPClient('https://localhost:7637', 'test_db')
    assert isinstance(client, HTTPClient)


def test_httpclient_context_manager_closes_session():
    with HTTPClient('https://localhost:7637', 'test_db') as client:
        assert isinstance(client, HTTPClient)
        assert not client._session.is_closed
    assert client._session.is_closed


def test_httpclient_close_method():
    client = HTTPClient('https://localhost:7637', 'test_db')
    client.close()
    assert client._session.is_closed
