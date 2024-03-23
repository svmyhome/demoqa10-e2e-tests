import requests
import pytest
from requests import Response
from jsonschema import validate

from schemas import reqres_schemas


@pytest.mark.positive
def test_update_user_put(base_url):
    schema = reqres_schemas.update_user
    payload = {"name": "morpheus1", "job": "leader1"}

    response: Response = requests.put(f'{base_url}users/2', json=payload)

    assert response.status_code == 200
    validate(response.json(), schema)
    assert response.json()['name'] == 'morpheus1'
    assert response.json()['job'] == 'leader1'


@pytest.mark.positive
def test_update_user_patch(base_url):
    schema = reqres_schemas.update_user_patch
    payload = {"name": "morpheus1", "job": "leader1"}
    payload_patch = {"name": "morpheus1", "job1": "leader1"}

    response: Response = requests.put(f'{base_url}users/2', json=payload)
    response: Response = requests.patch(f'{base_url}users/2', json=payload_patch)

    assert response.status_code == 200
    validate(response.json(), schema)
    assert response.json()['name'] == 'morpheus1'
    assert response.json()['job1'] == 'leader1'
