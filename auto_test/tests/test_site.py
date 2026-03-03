from selenium.webdriver.common.by import By
import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    #driver.find_element(By.XPATH, "//a[text()='Monitors']").click()
    #monitor_link = driver.find_element(By.XPATH, "//a[text()='Monitors']")
    #monitor_link.click()
    time.sleep(3)
    homepage.check_products_count(2)
    #monitors = driver.find_elements(By.CSS_SELECTOR, ".card")
    #assert len(monitors) == 2