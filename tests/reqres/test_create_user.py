import requests
import pytest
from requests import Response
from jsonschema import validate

from schemas import reqres_schemas


@pytest.mark.positive
def test_create_user_post(base_url):
    schema = reqres_schemas.create_user
    payload = {"name": "morpheus", "job": "leader"}

    response: Response = requests.post(f'{base_url}users', json=payload)

    assert response.status_code == 201
    validate(response.json(), schema)
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'
    assert response.json()['id'] is not None
    assert response.json()['createdAt'] is not None
