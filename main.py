from selenium import webdriver
from selenium.webdriver.common.by import By as by
import time


def main():
    driver = webdriver.Firefox()
    driver.get("https://example.com")
    h1 = driver.find_element(by.TAG_NAME, "h1")
    print(h1.text)
    time.sleep(2)
    driver.close()


if __name__ == "__main__":
    main()
