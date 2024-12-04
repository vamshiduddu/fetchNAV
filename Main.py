from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize FastAPI
app = FastAPI()

@app.get("/fetch-nav")
def fetch_nav():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for cloud environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Set up ChromeDriver
    service = Service("/usr/bin/chromedriver")  # Path to ChromeDriver in your server
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the webpage
        driver.get("https://www.morningstar.in/insurance/f00001obb3/Tata-AIA-Life-Nifty-Alpha-50-Index-Fund/detailed-portfolio.aspx")
        
        # Wait for the element to load
        wait = WebDriverWait(driver, 10)
        nav_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sal-dp-value")))
        
        # Extract NAV and 1-day return
        nav_text = nav_element.text
        nav_value, return_value = nav_text.split(" / ")
        nav_value = nav_value.strip()
        return_value = return_value.strip()

        return {
            "nav": nav_value,
            "one_day_return": return_value
        }
    except Exception as e:
        return {"error": str(e)}
    finally:
        driver.quit()
