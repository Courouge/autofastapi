import pytest

def test_read_main():
    response = requests.get("http://localhost:8000/")
    assert response.status_code == 200
    return 200
