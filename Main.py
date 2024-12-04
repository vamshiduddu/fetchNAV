from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed

try:
    # Open the target URL
    driver.get("https://www.morningstar.in/insurance/f00001obb3/Tata-AIA-Life-Nifty-Alpha-50-Index-Fund/detailed-portfolio.aspx")
    
    # Wait for the element to load (up to 10 seconds)
    wait = WebDriverWait(driver, 10)
    nav_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sal-dp-value")))
    
    # Extract NAV and 1-day return
    nav_text = nav_element.text
    nav_value, return_value = nav_text.split(" / ")

    # Clean and print the extracted values
    nav_value = nav_value.strip()
    return_value = return_value.strip()

    print(f"NAV: {nav_value}")
    print(f"1-Day Return: {return_value}")

finally:
    # Close the browser
    driver.quit()
