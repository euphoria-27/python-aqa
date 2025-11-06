import time
from pages.practice import QaPractice

def test_simple_button_click(driver):
    practice = QaPractice(driver)
    practice.open_simple_button()
    practice.click_simple_button()
    practice.check_submitted_text()