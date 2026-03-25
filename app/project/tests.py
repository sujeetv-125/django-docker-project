import pytest
from django.test import Client

@pytest.fixture
def client():
    return Client()

def test_admin_redirects(client):
    response = client.get('/admin/')
    assert response.status_code == 302

def test_404_on_unknown_path(client):
    response = client.get('/nonexistent/')
    assert response.status_code == 404
