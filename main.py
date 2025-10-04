from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxoptions
from selenium.webdriver.common.by import By as by
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from abc import ABC, abstractmethod



class Site(ABC):

    @abstractmethod
    def __init__(self, driver: webdriver.Firefox) -> None:
        pass

    @abstractmethod
    def getDriver(self) -> webdriver.Firefox:
        pass

    @abstractmethod
    def setDriver(self, driver: webdriver.Firefox) -> None:
        pass

    @abstractmethod
    def getSite(self) -> str:
        pass

    @abstractmethod
    def getSiteData(self) -> WebElement|None:
        pass

    @abstractmethod
    def fetchData(self) -> bool:
        pass


class Alko(Site):

    def __init__(self, driver: webdriver.Firefox) -> None:
        self.driver = driver
        self.site = "https://alko.fi"
        self.siteData = None

    def fetchData(self) -> bool:
        d = self.driver
        d.get(self.site)
        wait = WebDriverWait(d, 10)
        wait.until(ec.element_to_be_clickable((by.ID, "onetrust-reject-all-handler"))).click()
        wait.until(ec.invisibility_of_element_located((by.CLASS_NAME, "onetrust-pc-dark-filter")))
        wait.until(ec.element_to_be_clickable((by.CLASS_NAME, "icon-search-white-thin"))).click()
        links = wait.until(ec.visibility_of_all_elements_located((by.CLASS_NAME, "top-category-link")))
        for i in links:
            print(i.text)
        return True

    def getDriver(self): return self.driver
    def setDriver(self, driver): self.driver = driver
    def getSite(self): return self.site
    def getSiteData(self) -> WebElement|None: return self.siteData


class Skauppa(Site):

    def __init__(self, driver):
        self.driver = driver
        self.site = "https://s-kaupat.fi"


class Kkauppa(Site):

    def __init__(self, driver):
        self.driver = driver
        self.site = "https://k-ruoka.fi/kauppa"


def main():
    options = firefoxoptions()
    options.add_argument("--headless")

    with webdriver.Firefox(options) as driver:
        sites = [Alko(driver)]
        
        for i in sites:
            print(i.getSite())
            i.fetchData()


if __name__ == "__main__":
    main()
