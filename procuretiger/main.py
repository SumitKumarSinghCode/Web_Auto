from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://jewel-auction.procuretiger.com/JEWEL/pagenotfound#")
driver.maximize_window()

driver.find_element(By.ID,"loginLink").click()
driver.find_element(By.ID,"j_username").send_keys("balkishan100ni@gmail.com")
driver.find_element(By.ID,"j_password").send_keys("Sanjay@1234")
driver.find_element(By.NAME,"btnlogin").click()
driver.find_element(By.ID,"popup_ok").click()
driver.find_element(By.ID,"hrefManageAuction").click()
driver.find_element(By.ID,"link_66").click()
Auction_details = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/section/div[2]/div/table/tbody/tr[2]/td[2]/div/p")
print(Auction_details.text)



time.sleep(200)
driver.quit()