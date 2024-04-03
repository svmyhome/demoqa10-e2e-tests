import json
import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from requests import Response


def request_post_step_logging(url, **kwargs):
    with step(f"POST {url}"):
        response: Response = requests.post(f'{url}', **kwargs)
        request_to_curl = curlify.to_curl(response.request)
        logging.info(request_to_curl)
        logging.info(f'{response.text}')
        allure.attach(
            body=request_to_curl,
            name="request",
            attachment_type=allure.attachment_type.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4),
                name="response",
                attachment_type=allure.attachment_type.JSON,
                extension='json',
            )
        except:
            allure.attach(
                body=response.text,
                name="response",
                attachment_type=allure.attachment_type.TEXT,
                extension='txt',
            )
        return response


def request_put_step_logging(url, **kwargs):
    with step(f"PUT {url}"):
        response: Response = requests.put(f'{url}', **kwargs)
        request_to_curl = curlify.to_curl(response.request)
        logging.info(request_to_curl)
        logging.info(f'{response.text}')
        allure.attach(
            body=request_to_curl,
            name="request",
            attachment_type=allure.attachment_type.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4),
                name="response",
                attachment_type=allure.attachment_type.JSON,
                extension='json',
            )
        except:
            allure.attach(
                body=response.text,
                name="response",
                attachment_type=allure.attachment_type.TEXT,
                extension='txt',
            )
        return response


def response_logging(url, method, **kwargs):
    if method == 'POST':
        response: Response = requests.post(f'{url}', **kwargs)
    if method == 'GET':
        response: Response = requests.get(f'{url}', **kwargs)
    if method == 'PUT':
        response: Response = requests.put(f'{url}', **kwargs)
    if method == 'PATCH':
        response: Response = requests.patch(f'{url}', **kwargs)
    if method == 'DELETE':
        response: Response = requests.delete(f'{url}', **kwargs)
    return attach_info(response)


def attach_info(response: Response):
    with step(f"{response.request.method} {response.url}"):
        request_to_curl = curlify.to_curl(response.request)
        allure.attach(
            body=request_to_curl,
            name="request",
            attachment_type=allure.attachment_type.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4),
                name="response",
                attachment_type=allure.attachment_type.JSON,
                extension='json',
            )
        except:
            allure.attach(
                body=response.text,
                name="response",
                attachment_type=allure.attachment_type.TEXT,
                extension='txt',
            )
        return response


def request_patch_step_logging(url, **kwargs):
    with step(f"PATCH {url}"):
        response: Response = requests.patch(f'{url}', **kwargs)
        request_to_curl = curlify.to_curl(response.request)
        logging.info(request_to_curl)
        logging.info(f'{response.text}')
        allure.attach(
            body=request_to_curl,
            name="request",
            attachment_type=allure.attachment_type.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4),
                name="response",
                attachment_type=allure.attachment_type.JSON,
                extension='json',
            )
        except:
            allure.attach(
                body=response.text,
                name="response",
                attachment_type=allure.attachment_type.TEXT,
                extension='txt',
            )
        return response


def request_get_step_logging(url, **kwargs):
    with step(f"GET {url}"):
        response: Response = requests.get(f'{url}', **kwargs)
        request_to_curl = curlify.to_curl(response.request)
        logging.info(request_to_curl)
        logging.info(f'{response.text}')
        allure.attach(
            body=request_to_curl,
            name="request",
            attachment_type=allure.attachment_type.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4),
                name="response",
                attachment_type=allure.attachment_type.JSON,
                extension='json',
            )
        except:
            allure.attach(
                body=response.text,
                name="response",
                attachment_type=allure.attachment_type.TEXT,
                extension='txt',
            )
        return response


def request_delete_step_logging(url, **kwargs):
    with step(f"DELETE {url}"):
        response: Response = requests.delete(f'{url}', **kwargs)
        request_to_curl = curlify.to_curl(response.request)
        logging.info(request_to_curl)
        logging.info(f'{response.text}')
        request_to_curl = curlify.to_curl(response.request)
        allure.attach(
            body=request_to_curl,
            name="request",
            attachment_type=allure.attachment_type.TEXT,
            extension='txt',
        )
        try:
            allure.attach(
                body=json.dumps(response.json(), indent=4),
                name="response",
                attachment_type=allure.attachment_type.JSON,
                extension='json',
            )
        except:
            allure.attach(
                body=response.text,
                name="response",
                attachment_type=allure.attachment_type.TEXT,
                extension='txt',
            )
        return response
