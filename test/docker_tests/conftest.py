import pytest
import lynse
import time

@pytest.fixture(scope="session", autouse=True)
def start_server():
    lynse.launch_in_jupyter()
    time.sleep(1)
    yield
