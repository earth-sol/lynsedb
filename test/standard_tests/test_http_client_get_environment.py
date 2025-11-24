import httpx
from lynse.api.http_api.client_api import HTTPClient
from lynse.api.http_api.http_api.app import app


def test_http_client_get_environment_matches_route():
    transport = httpx.WSGITransport(app=app)
    with httpx.Client(transport=transport, base_url='http://testserver') as session:
        client = HTTPClient('http://testserver', 'test_db')
        client.set_test_session(session)
        direct_resp = session.get('/get_environment')
        assert direct_resp.status_code == 200
        direct_json = direct_resp.json()
        client_json = client.get_environment()
        assert client_json == direct_json
