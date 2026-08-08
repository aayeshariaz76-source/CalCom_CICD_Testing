from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calcom_event():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://cal.com/ayesha-riaz-r21oda/testing-event")

        wait = WebDriverWait(driver, 20)

        wait.until(
            EC.title_contains("Testing Event")
        )
        print("PASS: Testing Event page opened")

        slot = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[normalize-space()='9:00am']")
            )
        )

        assert slot.is_displayed()
        print("PASS: 9:00am slot located")

        assert "cal.com" in driver.current_url
        print("PASS: Cal.com URL verified")

    finally:
        driver.quit()
        print("PASS: Browser closed")