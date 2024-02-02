import time

import requests
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

os.chdir('../resources')
PROJECT_ROOT_PATH = os.getcwd()
# download with request
url = 'https://raw.githubusercontent.com/pytest-dev/pytest/main/doc/en/img/pytest_logo_curves.svg'

response = requests.get(url)
context = response.content

with open(
    os.path.join(PROJECT_ROOT_PATH, 'pytest_logo_curves.svg'), 'wb'
) as image_file:
    image_file.write(context)

url_2 = 'https://raw.githubusercontent.com/pytest-dev/pytest/main/CODE_OF_CONDUCT.md'

response = requests.get(url_2, allow_redirects=True)
context_2 = response.content
if response.history:
    print('Редиректы:')
    for r in response.history:
        print(r.url)

with open(os.path.join(PROJECT_ROOT_PATH, 'LICENSE'), 'wb') as text_file:
    text_file.write(context_2)

url_3 = 'https://raw.githubusercontent.com/pytest-dev/pytest/blob/main/AUTHORS'

response = requests.get(url_3, allow_redirects=True)
print(response.history)

with open(os.path.join(PROJECT_ROOT_PATH, 'AUTHOR'), 'wb') as text_file:
    text_file.write(response.content)

# download with selenium webdriver

locator = '[data-testid=download-raw-button]'
url_selenium = 'https://github.com/pytest-dev/pytest/blob/main/README.rst'

option = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "/home/vladimir/Downloads/Repository/PetProjects/Python/demoqa10-e2e-tests/resources",
    "download.prompt_for_download": False,
}
option.add_experimental_option("prefs", prefs)

driver_binary_path = ChromeDriverManager.install()
driver = webdriver.Chrome(service=Service(driver_binary_path), options=option)
browser.config.driver = driver

browser.open(url_selenium)
browser.element(locator).click()
time.sleep(4)
browser.close()

with open(os.path.join(PROJECT_ROOT_PATH, 'README.rst')) as file:
    # print(file.read())
    assert 'Support pytest' in file.read()
