# # import selenium
# #
# # selenium.webdriver.support.expected_conditions
# #
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.wait import WebDriverWait
# #
# #
# # class HomePage():
# #     lnk_account_xpath="//span[contains(text(),'My Account')]"
# #     lnk_register_linktext="//a[normalize-space()='Register']"
# #     lnk_login_linktext="//a[normalize-space()='Login']"
# #
# #     def __init__(self,driver):
# #         self.driver=driver
# #
# #     # def clickMyAccount(self):
# #     #
# #     #     self.driver.find_element(By.XPATH,self.lnk_account_xpath).click()
# #
# #     def clickMyAccount(self):
# #         # Wait for the element to be clickable
# #         WebDriverWait(self.driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, self.lnk_account_xpath))
# #         )
# #         # Click on the element
# #         self.driver.find_element(By.XPATH, self.lnk_account_xpath).click()
# #
# #     def clickRegister(self):
# #         self.driver.find_element(By.XPATH,self.lnk_register_linktext).click()
# #
# #     def clickLogin(self):
# #         self.driver.find_element(By.XPATH,self.lnk_login_linktext).click()
#
#
# # Remove the deprecated import statement for EC from telnetlib
# # from telnetlib import EC
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC  # Correct import statement for EC
#
# class HomePage():
#     lnk_account_xpath="//span[contains(text(),'My Account')]"
#     lnk_register_linktext="//a[normalize-space()='Register']"
#     lnk_login_linktext="//a[normalize-space()='Login']"
#
#     def __init__(self, driver):
#         self.driver=driver
#
#     def clickMyAccount(self):
#         # Wait for the element to be clickable
#         WebDriverWait(self.driver, 50).until(
#             EC.element_to_be_clickable((By.XPATH, self.lnk_account_xpath))
#         )
#         # Click on the element
#         self.driver.find_element(By.XPATH, self.lnk_account_xpath).click()
#
#     def clickRegister(self):
#         self.driver.find_element(By.XPATH,self.lnk_register_linktext).click()
#
#     def clickLogin(self):
#         self.driver.find_element(By.XPATH,self.lnk_login_linktext).click()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():
    lnk_account_xpath = "//span[contains(text(),'My Account')]"
    lnk_register_linktext = "//a[normalize-space()='Register']"
    lnk_login_linktext = "//a[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        # Wait for the element to be clickable
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.lnk_account_xpath))
            )
            element.click()
        except Exception as e:
            print(f"Exception occurred: {e}")

    def clickRegister(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.lnk_register_linktext))
            )
            element.click()
        except Exception as e:
            print(f"Exception occurred: {e}")

    def clickLogin(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.lnk_login_linktext))
            )
            element.click()
        except Exception as e:
            print(f"Exception occurred: {e}")
