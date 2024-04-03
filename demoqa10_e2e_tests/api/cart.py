import os

import allure
from allure_commons._allure import step
from selene import browser

from demoqa10_e2e_tests.utils import data, support_methods
from demoqa10_e2e_tests.utils.data import desktop_payload
from demoqa10_e2e_tests.utils.step_logging import response_logging


class Cart:

    @staticmethod
    def add_item(item, resource, payload=None):
        url_item = f"{os.getenv('WEB_URL')}{data.addproducttocart}{resource}/{item}"
        auth = support_methods.get_authorize_cookie()
        with allure.step('Add item to cart'):
            if payload:
                response_logging(
                    'POST',
                    url=url_item,
                    cookies={"NOPCOMMERCE.AUTH": auth},
                    data=payload,
                )
            else:
                response_logging(
                    'POST',
                    url=url_item,
                    cookies={"NOPCOMMERCE.AUTH": auth},
                )


cart = Cart()
