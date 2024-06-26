import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "https://demo.dealsdray.com/"
driver.get(url)
driver.maximize_window()


#USERNAME Input
username_path = "/html/body/div/div/div/div/div[2]/div/form/div[1]/div/div/input"
username = "prexo.mis@dealsdray.com"
input_element = driver.find_element(By.XPATH, username_path)
input_element.clear()
input_element.send_keys(username)


#PASSWORD Input
password_path = "/html/body/div/div/div/div/div[2]/div/form/div[2]/div/div/input"
password = "prexo.mis@dealsdray.com"
input_element = driver.find_element(By.XPATH, password_path)
input_element.clear()
input_element.send_keys(password)


#LOGIN
button1 = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div/form/div[3]/div/button")
button1.click()
time.sleep(5)


#DASHBOARD
dashboard = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div/div[2]/div[1]/div[2]/button")
dashboard.click()
orders = driver.find_element((By.XPATH),"/html/body/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/a/button")
orders.click()
time.sleep(4)


#ADD BULK ORDERS
add_bulk_orders = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[2]/button")
add_bulk_orders.click()
time.sleep(5)


#INPUT/UPLOAD XLS FILE
file_input_element = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/input")
file_path = "./demo-data.xlsx"
abs_file_path = os.path.abspath(file_path)
file_input_element.send_keys(abs_file_path)
import_element = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div[2]/div[3]/button")
import_element.click()
time.sleep(3)
validate_element = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div[2]/div[3]/button")
validate_element.click()
time.sleep(4)


# CLICK OK FOR ALERT POPUP
alert = driver.switch_to.alert
alert.accept()
print("Clicked OK on the alert.")
time.sleep(10)
total_width = driver.execute_script("return document.body.scrollWidth")
total_height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(total_width, total_height)


#SAVE SCREENSHOT OF THW WEBPAGE
save_path = "full_page_screenshot.png"
driver.save_screenshot(save_path)
print(f"Screenshot saved to {save_path}")
submit_element = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/button")
submit_element.click()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)


driver.quit()
