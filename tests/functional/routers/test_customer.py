import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

@pytest.mark.skip(reason="Mock database is not inplemented yet.")
def test_read_item():
    response = client.get("/customer/items")
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}