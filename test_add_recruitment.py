import time

from utils.browser import launch_browser
from Library.LoginPage import LoginPage
from Library.Recruitment import recruitment
from Library.HomePage import HomePage
from Library.Date import Currentdate


def test_add_recruitment():

    driver = launch_browser()

    Login = LoginPage(driver)
    Home = HomePage(driver)
    Recruitment = recruitment(driver)

    Login.Enter_Username("Admin")
    Login.Enter_Password("admin123")
    Login.Enter_Submit()

    Home.recruitment()

    Recruitment.add()

    Recruitment.FirstName("Naruto")
    Recruitment.LastName("Uzumaki")

    Recruitment.select_vacancy("Senior QA Lead")

    Recruitment.Email("asta@gmail.com")

    Recruitment.ContactNumber("1234567890")

    Recruitment.Upload_File(
        r'C:\Users\Hariharanpichayya\Downloads\Resume_MugundhanS.pdf'
    )

    Date = Currentdate.currentdate(0)

    Recruitment.Date_Of_Application(Date)

    Recruitment.Submit()

    Recruitment.Shortlist()

    print("Candidate Shortlisted successfully")

    Recruitment.Submit()

    time.sleep(10)

    driver.quit()