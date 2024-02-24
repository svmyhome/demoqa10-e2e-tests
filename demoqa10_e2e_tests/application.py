from components.left_panel import LeftPanel
from demoqa10_e2e_tests.pages.profile_page import ProfilePage
from demoqa10_e2e_tests.pages.text_box_registration_page import TextBoxRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simple_registration_page = TextBoxRegistrationPage()
        self.left_panel = LeftPanel()
        self.profile = ProfilePage()


app = ApplicationManager()
