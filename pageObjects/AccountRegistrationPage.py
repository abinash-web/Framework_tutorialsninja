from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_telephone_number = "telephone"
    txt_password_name = "password"
    txt_passwordConfirm_name = "confirm"
    click_policy_xpath = "//input[@name='agree']"
    btn_cont_xpath = "//input[@value='Continue']"
    text_msg_conf_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(fname)

    def setLastName(self, lame):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lame)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def set_telephone(self, phonenumber):
        self.driver.find_element(By.NAME, self.txt_telephone_number).send_keys(phonenumber)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def setconformPassword(self, confpwd):
        self.driver.find_element(By.NAME, self.txt_passwordConfirm_name).send_keys(confpwd)

    def setPrivatePolicy(self):
        self.driver.find_element(By.XPATH, self.click_policy_xpath).click()

    def clickconcontinue(self):
        self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()

    def getconfirmation(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_msg_conf_xpath).text
        except:
            None

# from selenium.common import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class AccountRegistrationPage:
#     txt_firstname_name = "firstname"
#     txt_lastname_name = "lastname"
#     txt_email_id = "email"
#     txt_telephone_name = "telephone"
#     txt_password_name = "password"
#     txt_confirm_name = "confirm"
#     chk_privacy_xpath = "//input[@type='checkbox']"
#     btn_continue_xpath = "//input[@type='submit']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # def setFirstName(self, fname):
#     #     element = WebDriverWait(self.driver, 10).until(
#     #         EC.visibility_of_element_located((By.NAME, self.txt_firstname_name))
#     #     )
#     #     element.send_keys(fname)
#     def setFirstName(self, fname):
#         try:
#             element = WebDriverWait(self.driver, 20).until(
#                 EC.visibility_of_element_located((By.NAME, self.txt_firstname_name))
#             )
#             element.send_keys(fname)
#         except TimeoutException as e:
#             print(f"TimeoutException occurred while setting first name: {e}")
#             # Handle the exception as needed (e.g., logging, retrying, failing the test)
#
#     def setLastName(self, lname):
#         element = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.NAME, self.txt_lastname_name))
#         )
#         element.send_keys(lname)
#
#     def setEmail(self, email):
#         element = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.ID, self.txt_email_id))
#         )
#         element.send_keys(email)
#
#     def setPassword(self, password):
#         element = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.NAME, self.txt_password_name))
#         )
#         element.send_keys(password)
#
#     def setConfirmPassword(self, confirm):
#         element = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.NAME, self.txt_confirm_name))
#         )
#         element.send_keys(confirm)
#
#     def setPrivatePolicy(self):
#         element = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, self.chk_privacy_xpath))
#         )
#         element.click()
#
#     def clickContinue(self):
#         element = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, self.btn_continue_xpath))
#         )
#         element.click()
#
#     def getConfirmationMessage(self):
#         element = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//h1[text()='Your Account Has Been Created!']"))
#         )
#         return element.text.strip()
