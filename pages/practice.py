from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class QaPractice:

    def __init__(self, driver):
        self.driver = driver
        
    def open(self):
        self.driver.get('https://www.qa-practice.com')

    def open_simple_button(self):
        self.driver.get('https://www.qa-practice.com/elements/button/simple')

    def open_single_checkbox(self):
        self.driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    def open_mult_checkbox(self):
        self.driver.get('https://www.qa-practice.com/elements/checkbox/mult_checkbox')

    def click_simple_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit-id-submit"))
        )
        self.driver.execute_script("arguments[0].click();", button)

    def check_submitted_text(self):
        submit_text = self.driver.find_element(By.CSS_SELECTOR, '.result-text')
        assert submit_text.text == 'Submitted'

    def click_mult_checkbox(self, checkbox):
        label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//label[@class="form-check-label" and contains(text(), "{checkbox}")]'))
        )
        label.click()

        chb = self.driver.find_element(By.ID, label.get_attribute('for'))
        
        assert chb.is_selected() == True