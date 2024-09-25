from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&ifkv=ARpgrqem8Td-HOX2AkBbgBX0gm-07qCEK8XrJyzy5AFXAvgpMfEGKuWZa0DZ6n_aNP15Ex6nYemGQw&ddm=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.maximize_window()

driver.find_element(By.ID,"identifierId").send_keys("sumitsingh993126@gmail.com")
driver.find_element(By.XPATH,"(//div[@class='VfPpkd-RLmnJb'])[2]")

time.sleep(200)
driver.quit()