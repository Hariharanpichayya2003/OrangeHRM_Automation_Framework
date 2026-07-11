from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import launch_browser
from Library.Actions import actions


class HomePage(actions):

    Recruitment = (By.XPATH,"//span[text()='Recruitment']")

    Performance = (By.XPATH,"//span[text()='Performance']")



    def __int__(self,driver):

        self.driver = driver

    def recruitment(self):

        self.click(self.Recruitment)
        print("Entered to Recruitment Page")

    def performance(self):

        self.click(self.Performance)
        print("Entered to Performance Page")