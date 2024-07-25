import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app
from app.crud import get_items as crud_get_items
from app.dependency import get_db as dependency_get_db

client = TestClient(app)

@pytest.fixture
def mock_get_db():
    with patch('app.dependency.get_db') as mock:
        yield mock

@pytest.fixture
def mock_get_items():
    with patch('app.crud.get_items') as mock:
        yield mock

def test_read_items(mock_get_db, mock_get_items):
    # Mocking the database session
    mock_db = MagicMock()
    mock_get_db.return_value = mock_db

    # Mocking the return value of crud.get_items
    mock_items = [
        {
            "id": 1,
            "name": "Item 1",
            "category": "Category 1",
            "description": "Description 1"
        },
        {
            "id": 2,
            "name": "Item 2",
            "category": "Category 2",
            "description": "Description 2"
        }
    ]
    mock_get_items.return_value = mock_items

    # Perform a GET request to the /items/ endpoint
    response = client.get("/customer/items/")

    # Assert the response status code and response data
    assert response.status_code == 200
    assert response.json() == mock_items