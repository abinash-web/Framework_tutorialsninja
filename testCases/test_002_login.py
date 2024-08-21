import pytest
import os
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities import randomeString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.readProperties import ReadConfig
class Test_login():
    baseURL = "https://tutorialsninja.com/demo/"
    logger = LogGen.loggen()

# baseUrl=ReadConfig.getApplicationURL()
    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*******Starting test_002_login*********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        #self.lp.SetEmail(self.user)
        self.lp.SetEmail("abinashgiri1997@gmail.com")
        self.lp.setPassword("Abinash@1997")
        #self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.targetpage=self.lp.ismyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
            assert False
            self.driver.close()
            self.logger.info("*******End of test_002_login********")