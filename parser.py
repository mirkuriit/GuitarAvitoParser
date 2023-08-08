from guitar import Guitar
from settings import Settings
from stypes import Stypes
from time_dec import fet

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

stypes: Stypes = Stypes()


class Parser:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Firefox(options=self.options)

    def __get_parse_link(self) -> str:
        s = f"https://www.avito.ru/{self.settings.city}/muzykalnye_instrumenty/gitary_i_strunnye-ASgBAgICAUTEAsYK?" \
            f"q={self.settings.q}" \
            f"&s={self.settings.sort_by}" \
            f"&f={self.settings.new_guitar}"
        print(s)
        return f"https://www.avito.ru/{self.settings.city}/muzykalnye_instrumenty/gitary_i_strunnye-ASgBAgICAUTEAsYK?" \
            f"q={self.settings.q}" \
            f"&s={self.settings.sort_by}" \
            f"&f={self.settings.new_guitar}"

    @fet
    def parse_guitar(self) -> list[Guitar]:
        self.browser.get(self.__get_parse_link())
        descr_class = "iva-item-descriptionStep-C0ty1"
        title_class = "iva-item-title-py3i_"
        price_class = "price-price-JP7qe"
        date_class = "iva-item-dateInfoStep-_acjp"
        ads = self.browser.find_elements(value="items-items-kAJAg", by=By.CLASS_NAME)
        native_ads = ads[0]
        all_native_ads_ids = native_ads.find_elements(by=By.CLASS_NAME,
                                                      value="iva-item-content-rejJg")
        parse_info = []
        for i, elem in enumerate(all_native_ads_ids):
            parse_info.append(Guitar(
                price=elem.find_element(by=By.CLASS_NAME, value=price_class).text,
                title=elem.find_element(by=By.CLASS_NAME, value=title_class).text,
                descr=elem.find_element(by=By.CLASS_NAME, value=descr_class).text,
                date=elem.find_element(by=By.CLASS_NAME, value=date_class).text,
                link=elem.find_element(by=By.CLASS_NAME, value=title_class).find_element(by=By.TAG_NAME,
                                                                                         value="a").get_attribute(
                    "href")
            ))
        return parse_info

















