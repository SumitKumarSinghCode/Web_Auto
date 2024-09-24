from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=ARpgrqeXkq5BtlZOUTlpaeHrFfON3_o2r30s5VXoKXu8FlU3TEqZok9appaRHZYyCNye5izfednfsg&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-47291469%3A1727170652967671&ddm=1")
driver.maximize_window()

driver.find_element(By.ID,"identifierId").send_keys("mailbox.prince.kumar@gmail.com")
driver.find_element(By.CSS_SELECTOR, "div[jsname = 'Njthtb']").click()

time.sleep(200)
driver.quit()