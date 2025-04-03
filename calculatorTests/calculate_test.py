from calculatorTests.basetest import BaseTest

class Test_Calculate(BaseTest):
    
    def test_add(self):
        self.initialize()
        self.calculatorPage.add("1", "1")
        assert self.calculatorPage.getResult().__contains__("2")
        
    def test_subtract(self):
        self.initialize()
        self.calculatorPage.subtract("5", "1")
        assert self.calculatorPage.getResult().__contains__("4")
        
    def test_multiply(self):
        self.initialize()
        self.calculatorPage.multiply("5", "5")
        assert self.calculatorPage.getResult().__contains__("25")
        
    def test_divide(self):
        self.initialize()
        self.calculatorPage.divide("10", "2")
        assert self.calculatorPage.getResult().__contains__("5")
        
