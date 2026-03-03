from selenium.webdriver.common.by import By
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def  open(self):
        self.driver.get("https://www.demoblaze.com/")

    def click_galaxy_s6(self):
        self.driver.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']").click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.XPATH, "//a[text()='Monitors']")
        monitor_link.click()

    def check_products_count(self, expected_count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(monitors) == expected_count