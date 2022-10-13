from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def find_elements_with_waiting(web_driver: WebDriver, wait_time: int, xpath: str):
    WebDriverWait(web_driver, wait_time).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return web_driver.find_elements("xpath", xpath)


class WhitebitParser:

    def __init__(self, web_driver: WebDriver):
        self.__driver = web_driver

    def get_exchange_rate_on_whitebit(self, from_currency: str, to_currency: str):
        exchange_code = f"{from_currency}-{to_currency}"
        whitebit_url = f"https://whitebit.com/ua/trade/{exchange_code}?tab=open-orders"
        if self.__driver.current_url != whitebit_url:
            self.__driver.get(whitebit_url)

        xpath = f"//a[@href='/ua/trade/{exchange_code}']/div[@title]"
        elements = find_elements_with_waiting(self.__driver, 10, xpath)
        if len(elements) >= 1:
            return elements[0].text
        else:
            raise Exception(f"Unable to get {exchange_code} exchange rate from whitebit exchange!")

    def get_exchange_rate_on_whitebit_threaded(self, from_currency: str, to_currency: str,
                                               thread_id: int, result_container: list):
        result_container[thread_id] = self.get_exchange_rate_on_whitebit(from_currency, to_currency)


class Offer:
    def __init__(self, price: float, available: float, limit_min: float, limit_max: float):
        self.price = price
        self.available = available
        self.limit_min = limit_min
        self.limit_max = limit_max


class BinanceParser:

    def __init__(self, web_driver: WebDriver):
        self.__driver = web_driver

    def get_sell_offers(self, bank_name: str):
        page_url = f"https://p2p.binance.com/ru-UA/trade/sell/USDT?fiat=UAH&payment={bank_name}"
        if self.__driver.current_url != page_url:
            self.__driver.get(page_url)
        items_path = "//div[@class=\'css-cjwhpx\']/div[@class=\'css-1mf6m87\']/div[@class=\'css-ovjtyv\']"
        elements = find_elements_with_waiting(self.__driver, 10, items_path)
        offers = [None] * len(elements)
        for i in range(len(elements)):
            price = float(elements[i].find_element("xpath", "/div/div/div/div/div[@class=\'css-1m1f8hn\']").text)
            available = float(str(elements[i].find_element("class", "css-vurnku").text).split(" ")[0])

        return offers
