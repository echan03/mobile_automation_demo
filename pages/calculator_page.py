from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class CalculatorPage(BasePage):
    
    def __init__(self, driver):
        self.driver = driver
        self.button_zero = '//android.widget.Button[@content-desc="0"]'
        self.button_one = '//android.widget.Button[@content-desc="1"]'
        self.button_two = '//android.widget.Button[@content-desc="2"]'
        self.button_three = '//android.widget.Button[@content-desc="3"]'
        self.button_four = '//android.widget.Button[@content-desc="4"]'
        self.button_five = '//android.widget.Button[@content-desc="5"]'
        self.button_six = '//android.widget.Button[@content-desc="6"]'
        self.button_seven = '//android.widget.Button[@content-desc="7"]'
        self.button_eight = '//android.widget.Button[@content-desc="8"]'
        self.button_nine = '//android.widget.Button[@content-desc="9"]'
        self.button_switch_plus_minus = '//android.widget.Button[@content-desc="Switch between plus and minus"]'
        self.button_decimal_point = '//android.widget.Button[@content-desc="Decimal point"]'
        self.button_division = '//android.widget.Button[@content-desc="Division"]'
        self.button_multiplication = '//android.widget.Button[@content-desc="Multiplication"]'
        self.button_minus = '//android.widget.Button[@content-desc="Minus"]'
        self.button_plus = '//android.widget.Button[@content-desc="Plus"]'
        self.button_equal = '//android.widget.Button[@content-desc="Equal"]'
        self.button_clear = '//android.widget.Button[@content-desc="Clear"]'
        self.button_brackets = '//android.widget.Button[@content-desc="Brackets"]'
        self.button_percentage = '//android.widget.Button[@content-desc="Percentage"]'
        self.editText_result = '//android.widget.EditText[@resource-id="com.sec.android.app.popupcalculator:id/calc_edt_formula"]'
        
    def pressButtons(self, equation):
        for char in equation:
            match char:
                case "0": self.click(AppiumBy.XPATH, self.button_zero)
                case "1": self.click(AppiumBy.XPATH, self.button_one)
                case "2": self.click(AppiumBy.XPATH, self.button_two)
                case "3": self.click(AppiumBy.XPATH, self.button_three)
                case "4": self.click(AppiumBy.XPATH, self.button_four)
                case "5": self.click(AppiumBy.XPATH, self.button_five)
                case "6": self.click(AppiumBy.XPATH, self.button_six)
                case "7": self.click(AppiumBy.XPATH, self.button_seven)
                case "8": self.click(AppiumBy.XPATH, self.button_eight)
                case "9": self.click(AppiumBy.XPATH, self.button_nine)
                case "+": self.click(AppiumBy.XPATH, self.button_plus)
                case "-": self.click(AppiumBy.XPATH, self.button_minus)
                case "*": self.click(AppiumBy.XPATH, self.button_multiplication)
                case "/": self.click(AppiumBy.XPATH, self.button_division)
                case "=": self.click(AppiumBy.XPATH, self.button_equal)
                case "c": self.click(AppiumBy.XPATH, self.button_clear)
                case "(" | ")": self.click(AppiumBy.XPATH, self.button_brackets)
                case "s": self.click(AppiumBy.XPATH, self.button_switch_plus_minus)
                case ".": self.click(AppiumBy.XPATH, self.button_decimal_point)
                case "%": self.click(AppiumBy.XPATH, self.button_percentage)
                
    def add(self, addend1, addend2):
        self.pressButtons(addend1)
        self.pressButtons("+")
        self.pressButtons(addend2)
        self.pressButtons("=")
        
    def subtract(self, minuend, subtrahend):
        self.pressButtons(minuend)
        self.pressButtons("-")
        self.pressButtons(subtrahend)
        self.pressButtons("=") 
        
    def multiply(self, factor1, factor2):
        self.pressButtons(factor1)
        self.pressButtons("*")
        self.pressButtons(factor2)
        self.pressButtons("=")
        
    def divide(self, dividend, divisor):
        self.pressButtons(dividend)
        self.pressButtons("/")
        self.pressButtons(divisor)
        self.pressButtons("=") 
    
    def getResult(self) -> str:
        return self.getText(AppiumBy.XPATH, self.editText_result)