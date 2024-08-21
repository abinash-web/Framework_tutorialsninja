import os.path

import pytest

from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities import randomeString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.readProperties import ReadConfig


class Test_001_AccountReg:
    baseURL = "https://tutorialsninja.com/demo/"
    logger=LogGen.loggen()

   # baseUrl=ReadConfig.getApplicationURL()
    @pytest.mark.regresstion
    def test_account_Reg(self, setup):
        self.logger.info("****test_001_AccountRegistration****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("****Lunching the application****")
        self.driver.maximize_window()


        self.hp = HomePage(self.driver)
        self.logger.info("clicking on My account->Register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()


        self.logger.info("Providing customer details for Registration ")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("Abinash")
        self.regpage.setLastName("Giri")
        self.email = randomeString.random_string_generator() + '@gmail.com'
        # self.regpage.setEmail("abc")

        self.regpage.setEmail(self.email)
        self.regpage.set_telephone("123456789")
        self.regpage.setPassword("1234567")
        self.regpage.setconformPassword("1234567")
        self.regpage.setPrivatePolicy()
        self.regpage.clickconcontinue()

        self.confnmsg = self.regpage.getconfirmation()

        if self.confnmsg == "Your Account Has Been Created!":
            self.logger.info("AccountRegistration has passed")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_failed1.png")
            self.logger.info("AccountRegistration has failed")
            self.driver.close()
            assert False
        self.logger.info("test_001_AccountRegistration is finshed")
