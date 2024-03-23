import requests
import pytest
from requests import Response


@pytest.mark.positive
def test_delete_user(base_url):
    response: Response = requests.delete(f'{base_url}users/2')
    assert response.status_code == 204
    assert response.text == ""
