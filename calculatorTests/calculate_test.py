import pytest
from calculatorTests.basetest import BaseTest

class Test_Calculate(BaseTest):
    
    @pytest.mark.smoke
    def test_add(self):
        self.pages["calculator_page"].add("1", "1")
        assert self.pages["calculator_page"].getResult().__contains__("2")
        
    @pytest.mark.smoke
    def test_subtract(self):
        self.pages["calculator_page"].subtract("5", "1")
        assert self.pages["calculator_page"].getResult().__contains__("4")
        
    @pytest.mark.smoke
    def test_multiply(self):
        self.pages["calculator_page"].multiply("5", "5")
        assert self.pages["calculator_page"].getResult().__contains__("25")
        
    @pytest.mark.smoke
    def test_divide(self):
        self.pages["calculator_page"].divide("10", "2")
        assert self.pages["calculator_page"].getResult().__contains__("5")
        
