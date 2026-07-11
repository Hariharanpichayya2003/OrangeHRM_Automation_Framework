from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import launch_browser
from Library.Actions import actions

class LoginPage(actions):

    ENTER_USERNAME = (By.NAME,"username")
    ENTER_PASSWORD = (By.NAME,"password")
    CLICK_BUTTON = (By.XPATH,"//button[@type='submit']")

    def __init__(self,driver):
        self.driver = driver

    def Enter_Username(self,username):
          self.entertext(self.ENTER_USERNAME,username)
          

    def Enter_Password(self,password):
        self.entertext(self.ENTER_PASSWORD,password)

    def Enter_Submit(self):
        self.click(self.CLICK_BUTTON)
        

