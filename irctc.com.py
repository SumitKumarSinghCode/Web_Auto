from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create an instance of ChromeOptions
chrome_options = webdriver.ChromeOptions()

# Get the path for the ChromeDriver
driver_path = ChromeDriverManager().install()

# Initialize the WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=chrome_options)

# Open the website
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='LOGIN']").click()

#driver.find_element(By.NAME, "userId").send_keys("sumit223345")

# Pause for 60 seconds to inspect the webpage manually
time.sleep(60)

# Close the browser
driver.quit()
