import pytest
import requests
from requests_mock.mocker import Mocker

@pytest.fixture
def mock_requests_get(mocker):
    response_json = {"businesses":[{"name":"Teton Elementary"}]}
    
    # Patching requests.get to return a mocked response
    mocker.patch.object(requests, 'get', return_value=MockResponse(response_json))

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def test_data_endpoint(mock_requests_get):

    response = requests.get('http://127.0.0.1:8000/users/')

    assert response.status_code == 200


    data = response.json()
    assert isinstance(data, dict)
    assert 'businesses' in data
    businesses = data['businesses']
    assert isinstance (businesses, list)
    assert len(businesses) > 0
    first_business = businesses[0]
    assert isinstance(first_business, dict)
    assert 'name' in first_business
    assert first_business['name'] == 'Teton Elementary'
