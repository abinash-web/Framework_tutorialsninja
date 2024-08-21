from datetime import datetime
import os

import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture()
# def setup():
#     Service_obj = Service()
#     driver = webdriver.Chrome(service=Service_obj)
#
#
#     return driver
@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching firefox browser.........")
    else:
        Service_obj = Service()
        driver = webdriver.Chrome(service=Service_obj)


    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")




########### pytest HTML Report ################

import os
from datetime import datetime
import pytest


# Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'


# Hook for delete/modify environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# Hook for specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Create reports directory if it doesn't exist
    os.makedirs(os.path.join(os.getcwd(), 'reports'), exist_ok=True)

    # Set HTML report path with timestamp
    timestamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    config.option.htmlpath = os.path.join(os.getcwd(), 'reports', f'report_{timestamp}.html')
