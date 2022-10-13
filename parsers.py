from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import re


def clear_float_value_from_text(text: str):
    return "".join(str(x) for x in re.findall("[0123456789.]", text))


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

    def __str__(self):
        return " ".join(str(x) for x in
                  ["Price:", self.price,
                  "Available:", self.available,
                  "Limit min:", self.limit_min,
                  "Limit max:", self.limit_max])


class BinanceParser:

    def __init__(self, web_driver: WebDriver):
        self.__driver = web_driver

    def __get_offer_from_web_element(self, offer_element: WebElement):
        self.__driver.execute_script("arguments[0].scrollIntoView();", offer_element)

        price_e = offer_element.find_element("xpath", ".//div[@class=\'css-1kj0ifu\']/div[@class=\'css-1m1f8hn\']")
        price = float(clear_float_value_from_text(price_e.text))

        available_e = offer_element.find_element("xpath", ".//div[@class=\'css-3v2ep2\']/div[@class=\'css-vurnku\']")
        available = float(clear_float_value_from_text(available_e.text))

        limit_es = offer_element.find_elements("xpath", ".//div[@class=\'css-4cffwv\']")
        limit_min = float(clear_float_value_from_text(limit_es[0].text))
        limit_max = float(clear_float_value_from_text(limit_es[1].text))
        return Offer(price, available, limit_min, limit_max)

    def __get_offers(self, binance_page_url: str):
        page_url = binance_page_url
        if self.__driver.current_url != page_url:
            self.__driver.get(page_url)

        items_path = "//div[@class=\'css-cjwhpx\']/div[@class=\'css-1mf6m87\']/div[@class=\'css-ovjtyv\']"
        offer_web_elements = find_elements_with_waiting(self.__driver, 10, items_path)
        offers = []
        for offer_web_element in offer_web_elements:
            offers.append(self.__get_offer_from_web_element(offer_web_element))
        return offers

    def get_sell_offers(self, from_currency, to_currency, bank_name):
        return self.__get_offers(
            f"https://p2p.binance.com/ru-UA/trade/sell/{from_currency}?fiat={to_currency}&payment={bank_name}")

    def get_buy_offers(self, from_currency, to_currency, bank_name):
        return self.__get_offers(
            f"https://p2p.binance.com/en/trade/{bank_name}/{from_currency}?fiat={to_currency}")
