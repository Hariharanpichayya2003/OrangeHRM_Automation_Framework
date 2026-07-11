from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import launch_browser

from Library.LoginPage import LoginPage

driver = launch_browser()

login = LoginPage(driver)

login.Enter_Username("ABCD")

login.Enter_Password("1234")

login.Enter_Submit()

message = WebDriverWait(driver,30).until(EC.visibility_of_element_located(( By.XPATH,"//p[contains(@class,'oxd-alert-content-text')]"))).text

assert "Invalid credentials" in message
print("Verification Success")

driver.quit()


