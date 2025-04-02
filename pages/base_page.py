from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.webelement import WebElement
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by: AppiumBy, locator: str):
        self.waitForElement(by, locator)
        self.driver.find_element(by, value=locator).click()
        
    def longPress(self, by: AppiumBy, locator: str):
        self.waitForElement(by, locator)
        element = self.driver.find_element(by, value=locator)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"), duration=1000)
        actions.w3c_actions.pointer_action.move_to_location(element.location["x"] + (element.size["width"] / 2) , element.location["y"] + (element.size["height"] / 2))
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(3)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def send_keys(self, by: AppiumBy, locator: str, content: str):
        self.driver.find_element(by, value=locator).send_keys(content)
        self.driver.hide_keyboard()
        
    def clear(self, by: AppiumBy, locator: str) :
        self.driver.find_element(by, value=locator).clear()
        self.driver.hide_keyboard()
  
    def waitForElement(self, by: AppiumBy, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout=timeout)
        wait.until(lambda d : self.driver.find_element(by, locator).is_displayed())
            
    def isElementDisplayed(self, by: AppiumBy, locator: str, timeout=5) -> bool :
        try:
            self.driver.implicitly_wait(timeout)
            return self.driver.find_element(by, locator).is_displayed()
        except NoSuchElementException:
            return False
        
    def scroll(self, topElementBy: AppiumBy, topElementLocator, bottomElementBy: AppiumBy, bottomElementLocator, direction="down"):
        bottomElement = self.driver.find_element(bottomElementBy, bottomElementLocator)
        topElement = self.driver.find_element(topElementBy, topElementLocator)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"), duration=1000)
        
        if(direction == "down"):
            actions.w3c_actions.pointer_action.move_to_location(bottomElement.location["x"] + (bottomElement.size["width"] / 2), bottomElement.location["y"] + (bottomElement.size["height"] / 2))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(topElement.location["x"] + (topElement.size["width"] / 2), topElement.location["y"] + (topElement.size["height"] / 2))
            actions.w3c_actions.pointer_action.release()
        else:
            actions.w3c_actions.pointer_action.move_to_location(topElement.location["x"] + (topElement.size["width"] / 2), topElement.location["y"] + (topElement.size["height"] / 2))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(bottomElement.location["x"] + (bottomElement.size["width"] / 2), bottomElement.location["y"] + (bottomElement.size["height"] / 2))
            actions.w3c_actions.pointer_action.release()
    
        actions.perform()
        
    def listScroll(self, listOfElements, direction: str = "down"):
        topElement = listOfElements[0]
        bottomElement = listOfElements[len(listOfElements) - 1]
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"), duration=1000)
        
        if(direction == "down"):
            actions.w3c_actions.pointer_action.move_to_location(bottomElement.location["x"] + (bottomElement.size["width"] / 2), bottomElement.location["y"] + (bottomElement.size["height"] / 2))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(topElement.location["x"] + (topElement.size["width"] / 2), topElement.location["y"] + (topElement.size["height"] / 2))
            actions.w3c_actions.pointer_action.release()
            
        else:
            actions.w3c_actions.pointer_action.move_to_location(topElement.location["x"] + (topElement.size["width"] / 2), topElement.location["y"] + (topElement.size["height"] / 2))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(bottomElement.location["x"] + (bottomElement.size["width"] / 2), bottomElement.location["y"] + (bottomElement.size["height"] / 2))
            actions.w3c_actions.pointer_action.release()
            
        actions.perform()
        
    def scrollOnElement(self, element, direction: str = "down"):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"), duration=1000)
        
        if(direction == "down"):
            actions.w3c_actions.pointer_action.move_to_location(element.location["x"], element.location["y"]  + element.size["height"])
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(element.location["x"], element.location["y"])
            actions.w3c_actions.pointer_action.release()
            
        else:
            actions.w3c_actions.pointer_action.move_to_location(element.location["x"], element.location["y"])
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(element.location["x"], element.location["y"] + element.size["height"])
            actions.w3c_actions.pointer_action.release()
            
        actions.perform()
        
    def selectTextFromPicker(self, topElementBy: AppiumBy, topElementLocator, bottomElementBy: AppiumBy, \
        bottomElementLocator, textToSelectBy: AppiumBy, textToSelectLocator, direction: str = "down") :
        retries = 0
        if self.isElementDisplayed(textToSelectBy, textToSelectLocator, timeout=2) == False :
            while(self.isElementDisplayed(textToSelectBy, textToSelectLocator, timeout=2) != True and retries < 20) :
                self.scroll(topElementBy, topElementLocator, bottomElementBy, bottomElementLocator, direction)
                retries = retries + 1
        self.click(textToSelectBy, textToSelectLocator)
        
    def scrollToCenter(self, \
        listOfElementsBy: AppiumBy, listOfElementsLocator, \
        textToSelectBy: AppiumBy, textToSelectLocator, \
        centerElementBy: AppiumBy, centerElementSelector, \
        direction: str = "down") :
        retries = 0
        isElementFound = False
        if self.isElementDisplayed(textToSelectBy, textToSelectLocator, timeout=2) == False :
            while isElementFound == False and retries < 20:
                elements = self.driver.find_elements(listOfElementsBy, listOfElementsLocator)
                self.listScroll(elements, direction)
                retries += 1
                isElementFound = self.isElementDisplayed(textToSelectBy, textToSelectLocator, timeout=2)
        self.scroll(centerElementBy, centerElementSelector, textToSelectBy, textToSelectLocator)
        
        
    def wait(self, seconds: float):
        time.sleep(seconds)
        
    def setRating(self, locatorBy: AppiumBy, locator: str, rating: int):
        element = self.driver.find_element(locatorBy, locator)
        startX = element.location["x"]
        endX = startX + element.size["width"]
        yAxis = element.location["y"]
        tapAt = endX * (rating / 5)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(startX, yAxis)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(tapAt, yAxis)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        
    def getText(self, locatorBy: AppiumBy, locator: str) -> str:
        return self.driver.find_element(locatorBy, locator).text
    
    def count(self, locatorBy: AppiumBy, locator: str) -> int:
        return len(self.driver.find_elements(locatorBy, locator))
    
    def getLastElementTextInList(self, locatorBy: AppiumBy, locator: str) -> str:
        elements = self.driver.find_elements(locatorBy, locator)
        count = len(elements)
        return elements[count - 1].text
    
    def getElementInPosition(self, locatorBy: AppiumBy, locator: str, index: int) -> WebElement:
        elements: WebElement = self.driver.find_elements(locatorBy, locator)
        return elements[index]
    
    def getElementHeight(self, element: WebElement) -> int:
        return element.size["height"]
    
    def isElementEnabled(self, locatorBy: AppiumBy, locator: str) -> bool:
        element = self.driver.find_element(locatorBy, locator)
        return element.is_enabled()
        