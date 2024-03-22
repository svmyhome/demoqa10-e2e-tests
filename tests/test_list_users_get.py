import requests
import pytest
from requests import Response
from jsonschema import validate

from tests import reqres_schemas

"""
Написать API-тесты:
1. на каждый из методов GET/POST/PUT/DELETE ручек reqres.in  +
2. Позитивные/Негативные тесты на одну из ручек.
3. На разные статус-коды 200/201/204/404/400  +
4. На разные схемы (4-5 схем) +
5. С ответом и без ответа
Дополнительно со * : 
6. На бизнес-логику (заметить какую-то фичу и автоматизировать, как делали на уроке)
Автотесты должны иметь говорящее название, которое будет понятно человеку не глядя в код.
"""

BASE_URL = 'https://reqres.in/api/'


def test_get_list_users():
    schema = reqres_schemas.list_users

    response: Response = requests.get(f'{BASE_URL}users', params={"page": 2})
    print(response.text)

    assert response.status_code == 200
    validate(response.json(), schema)


def test_post_create_user():
    schema = reqres_schemas.create_user
    payload = {"name": "morpheus", "job": "leader"}

    response: Response = requests.post(f'{BASE_URL}users', json=payload)
    print(response.text)

    assert response.status_code == 201
    validate(response.json(), schema)


def test_put_update_user():
    schema = reqres_schemas.update_user
    payload = {"name": "morpheus1", "job": "leader1"}

    response: Response = requests.put(f'{BASE_URL}users/2', json=payload)
    print(response.text)

    assert response.status_code == 200
    validate(response.json(), schema)


def test_patch_update_user():
    schema = reqres_schemas.update_user_patch
    payload = {"name": "morpheus1", "job": "leader1"}
    payload_patch = {"name": "morpheus1", "job1": "leader1"}

    response: Response = requests.put(f'{BASE_URL}users/2', json=payload)
    print(response.text)
    response: Response = requests.put(f'{BASE_URL}users/2', json=payload_patch)
    print(response.text)

    assert response.status_code == 200
    validate(response.json(), schema)


def test_delete_user():
    response: Response = requests.delete(f'{BASE_URL}users/2')
    print(response.text)
    assert response.status_code == 204


def test_get_list_user_not_found():
    schema = reqres_schemas.user_not_found

    response: Response = requests.get(f'{BASE_URL}users/2322')
    print(response.text)

    assert response.status_code == 404
    validate(response.json(), schema)


def test_post_register_negative():
    schema = reqres_schemas.register_user_fail
    payload = {"email": "sydney@fife"}

    response: Response = requests.post(f'{BASE_URL}register', json=payload)
    print(response.text)

    assert response.status_code == 400
    validate(response.json(), schema)
