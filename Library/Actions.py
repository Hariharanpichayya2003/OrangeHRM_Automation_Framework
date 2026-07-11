from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class actions:
    def __init__(self,driver):
        self.driver = driver

    def entertext(self,locator,text):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text)

    def click(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator))
        element.click()

    def custom_dropdown(self,locator,value):

        self.click(locator)

        option = (By.XPATH , f"//div[@role='option'] [normalize-space()='{value}']")

        self.click(option)

    def upload_file(self,locator,filepath):

        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))

        element.send_keys(filepath)
        print("File Uploaded Successfully")




        