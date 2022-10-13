from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WhitebitParser:

    def __init__(self, web_driver: WebDriver):
        self.__driver = web_driver

    @staticmethod
    def __find_elements_with_waiting(web_driver: WebDriver, wait_time: int, xpath: str):
        WebDriverWait(web_driver, wait_time) \
            .until(EC.presence_of_element_located((By.XPATH, xpath)))
        return web_driver.find_elements("xpath", xpath)

    def get_exchange_rate_on_whitebit(self, from_currency: str, to_currency: str):
        exchange_code = f"{from_currency}-{to_currency}"
        self.__driver.get(f"https://whitebit.com/ua/trade/{exchange_code}?tab=open-orders")
        elements = self.__find_elements_with_waiting(self.__driver, 2,
                                                     f"//a[@href='/ua/trade/{exchange_code}']/div[@title]")
        if len(elements) >= 1:
            return elements[0]
        else:
            raise Exception(f"Unable to get {exchange_code} exchange rate from whitebit exchange!")

