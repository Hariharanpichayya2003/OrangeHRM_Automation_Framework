
from Library.Actions import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Library.Date import Currentdate




class recruitment(actions):

    Add_button = (By.XPATH,"//button[text()=' Add ']")

    FirstName_Textbox = (By.XPATH,"//input[@name='firstName']")
    MiddleName_Textbox = (By.XPATH,"//input[@name='middleName']")
    LastName_Textbox = (By.XPATH,"//input[@name='lastName']")
    Email_Textbox = (By.XPATH,"//div[@class='oxd-form-row'][3]//input[1]")
    ContactNumber_Textbox = (By.XPATH,"//label[text()='Contact Number']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    Vacancy = ( By.XPATH, "//div[contains(@class,'oxd-select-text')]")
    UploadFile = (By.XPATH,"//input[@type='file']")
    DateOfApplication = (By.XPATH,"//input[@placeholder='yyyy-dd-mm']")
    Submitbutton = (By.XPATH,"//button[@type='submit']")

    Shortlistbutton = (By.XPATH,"//button[text()=' Shortlist ']")

    def __init__(self,driver):
        self.driver = driver

    def add(self):
        self.click(self.Add_button)
        print("Add button clicked")

    def FirstName(self,firstname):
        self.entertext(self.FirstName_Textbox,firstname)

    def MiddleName(self,middlename):
        self.entertext(self.MiddleName_Textbox,middlename)

    def LastName(self,lastname):
        self.entertext(self.LastName_Textbox,lastname)
        
    def select_vacancy(self,value):
        self.custom_dropdown(self.Vacancy,value)

    def Email(self,email):
        self.entertext(self.Email_Textbox,email)

    def ContactNumber(self,contactnumber):
        self.entertext(self.ContactNumber_Textbox,contactnumber)

    def Upload_File(self,filepath):
        self.upload_file(self.UploadFile,filepath)

    def Date_Of_Application(self,date):
        self.entertext(self.DateOfApplication,date)
    
    def Submit(self):
        self.click(self.Submitbutton)

    def Shortlist(self):
        self.click(self.Shortlistbutton)