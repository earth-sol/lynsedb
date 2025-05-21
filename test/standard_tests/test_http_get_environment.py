import pytest
from lynse.api.http_api.http_api.app import app
from lynse.configs.config import config


def test_get_environment_returns_config_values():
    with app.test_client() as client:
        resp = client.get('/get_environment')
        assert resp.status_code == 200
        params = resp.get_json()["params"]
        keys = ['LYNSE_LOG_LEVEL', 'LYNSE_LOG_PATH', 'LYNSE_TRUNCATE_LOG',
                'LYNSE_LOG_WITH_TIME', 'LYNSE_KMEANS_EPOCHS', 'LYNSE_SEARCH_CACHE_SIZE']
        expected = {key: getattr(config, key) for key in keys}
        assert params == expected
