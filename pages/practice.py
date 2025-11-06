from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QaPractice:

    def __init__(self, driver):
        self.driver = driver
        
    def open(self):
        self.driver.get('https://www.qa-practice.com')

    def open_simple_button(self):
        self.driver.get('https://www.qa-practice.com/elements/button/simple')

    def click_simple_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit-id-submit"))
        )
        self.driver.execute_script("arguments[0].click();", button)

    def check_submitted_text(self):
        submit_text = self.driver.find_element(By.CSS_SELECTOR, '.result-text')
        assert submit_text.text == 'Submitted'