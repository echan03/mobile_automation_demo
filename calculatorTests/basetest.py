import pytest
from pages.calculator_page import CalculatorPage

@pytest.mark.usefixtures("appium_driver")
@pytest.mark.usefixtures("appium_session")

class BaseTest:
    
    @pytest.fixture(autouse=True)
    def injector(self, pages):
        self.pages = pages