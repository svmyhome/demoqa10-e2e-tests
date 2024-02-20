from components.left_panel import LeftPanel
from demoqa10_e2e_tests.pages.registartion_page import RegistrationPage
from demoqa10_e2e_tests.pages.text_box_registration_page import TextBoxRegistrationPage


class ApplicationManager:


    def __init__(self):
        self.simple_registration_page = TextBoxRegistrationPage()
        self.full_registration_page = RegistrationPage()
        self.left_panel = LeftPanel()


app = ApplicationManager()