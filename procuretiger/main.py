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
#driver.find_element(By.XPATH,"//a[@id='link_67']").click() #Live
#driver.find_element(By.XPATH,"//*[@id='hrefManageAuction']").click() #Search Auction
#driver.find_element(By.XPATH,"//*[@id='link_66']").click() #My Auction
#driver.find_element(By.LINK_TEXT, "View Result").click()

#driver.find_element(By.XPATH,'//*[@id="reportDetail"]/tr[2]/td[2]/div/p/a[4]')





# To enter the value for Serial No. 1, input '2'.
# For Serial No. 2, enter '4', and continue this pattern for subsequent serial numbers.
# serial_number = int(input("Enter serial number of the bid :"))
# driver.find_element(By.XPATH,f"*[@id='reportDetail'']/tr[2]/td[1]") for serial number




time.sleep(200)
driver.quit()