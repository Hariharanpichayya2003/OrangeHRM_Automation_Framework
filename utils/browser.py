from selenium import webdriver

def launch_browser():

    driver = webdriver.Chrome()

    print("Chrome Opened")

    driver.maximize_window()

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    driver.get(url)

    print("Website Opened")

    return driver