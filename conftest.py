import time
import pytest
import os
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from pages.calculator_page import CalculatorPage

#declare page objects here
@pytest.fixture
def pages():
        calculator_page = CalculatorPage(driver)
        return locals()

@pytest.fixture(scope="session")
def appium_session():
    
    service_args = ["--address", "127.0.0.1", "-p", "4723"]
    service = AppiumService()
    service.start(args=service_args)
    if service.is_running:
        print("Appium server started successfully!") 
    yield service
    service.stop()
    
def pytest_addoption(parser):
    parser.addoption("--devicename", action="store", default="Android")  
    
@pytest.fixture(scope="function")
def appium_driver(request):
    
    global driver
    
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appPackage='com.sec.android.app.popupcalculator',
        appActivity='.Calculator',
        fastReset='true',
        language='en',
        locale='US',
        enableMultiWindows=True,
    )
    
    #capability to run in a specific device
    deviceSerial = request.config.getoption("--devicename")
    if deviceSerial == "galaxy_a51":
        deviceSerial = "RZ8NA1W972A"
        capabilities["udid"] = deviceSerial
    
    #capability for installing app
    # current_path = os.path.dirname(__file__)
    # app_path = '/apk/app-release.apk' if os.name == 'posix' else '\\apk\\app-release.apk'
    # capabilities["app"] = app_path
    
    appium_server_url = 'http://localhost:4723'
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    time.sleep(2)
    driver.quit()
    
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function", autouse=True)
def test_failed_check(appium_driver, request):
    yield
    if request.node.rep_setup.failed:
        print("Setting up test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            current_test_name = request.node.name
            now = datetime.now() 
            dt_string = now.strftime("%m-%d-%Y-%H-%M-%S")  
            appium_driver.save_screenshot(f'logs/{dt_string}_{current_test_name}_FAILED.png')
            print("Executing test failed", request.node.nodeid)