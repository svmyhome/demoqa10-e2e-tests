from selene import browser, have
import allure

from demoqa10_e2e_tests.test_data.users import SimpleUser


class ProfilePage:
    @allure.step('Checking submited user information')
    def should_have_submited_info(self, worker: SimpleUser):
        browser.all('#output p').should(
            have.exact_texts(
                f'Name:{worker.full_name}',
                f'Email:{worker.email}',
                f'Current Address :{worker.current_address}',
                f'Permananet Address :{worker.permanent_address}',
            )
        )
