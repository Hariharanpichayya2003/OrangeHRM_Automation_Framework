from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import launch_browser

from Library.LoginPage import LoginPage


def test_login_valid():

    driver = launch_browser()

    login = LoginPage(driver)

    login.Enter_Username("Admin")
    login.Enter_Password("admin123")
    login.Enter_Submit()

    Search = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'Search')]")
        )
    )

    assert Search.is_displayed()

    print("Login Successfully")

    driver.quit()