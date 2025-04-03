import pytest
from pages.calculator_page import CalculatorPage

@pytest.mark.usefixtures("appium_driver")
@pytest.mark.usefixtures("appium_session")
class BaseTest:
    def initialize(self):
        self.calculatorPage = CalculatorPage(self.driver)