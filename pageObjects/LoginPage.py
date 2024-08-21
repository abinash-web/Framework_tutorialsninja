from selenium.webdriver.common.by import By


class LoginPage():
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//input[@value='Login']"
    Account_verification = "//h2[normalize-space()='My Account']"

    #//h2[normalize-space()='My Account']

    def __init__(self, driver):
        self.driver = driver

    def SetEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def Setpassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def ismyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.Account_verification).is_displayed()
        except:
            return False
