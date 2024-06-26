import xlwt
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait

devices = {
    "Desktop": {
        "1920x1080": (1920, 1080),
        "1366x768": (1366, 768),
        "1536x864": (1536, 864)
    },
    "Mobile": {
        "360x640": (360, 640),
        "414x896": (414, 896),
        "375x667": (375, 667)
    }
}

# Set up the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

url = "https://www.getcalley.com/page-sitemap.xml"

# Navigate to the webpage
driver.get(url)

tbody = driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody")

rows = []

for i in tbody:
    rows += i.find_elements(By.TAG_NAME, "tr")
# rows = tbody.find_elements(By.TAG_NAME, 'tr')
# Loop through the rows and extract data

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Data')

sheet.write(0,0,"Link")
sheet.write(0,1,"Number of Pages")
sheet.write(0,2,"Date and Time (GMT)")

row_index = 1

for row in rows:
    # Extract the link
    link_element = row.find_element(By.XPATH, ".//td[1]/a")
    link = link_element.get_attribute('href')

    # Extract the number of images
    images_element = row.find_element(By.XPATH, ".//td[2]")
    number_of_images = images_element.text

    # Extract the date and time in GMT
    datetime_element = row.find_element(By.XPATH, ".//td[3]")
    datetime_gmt = datetime_element.text

    # Print the extracted information
    print(f"Link: {link}")
    print(f"Number of Images: {number_of_images}")
    print(f"Date and Time (GMT): {datetime_gmt}")
    print("-----")

    sheet.write(row_index,0,link)
    sheet.write(row_index,1,number_of_images)
    sheet.write(row_index,2,datetime_gmt)

    row_index += 1

workbook.save("data.xls")


def create_directories():
    for device in devices:
        for resolution in devices[device]:
            path = os.path.join(device, resolution)
            if not os.path.exists(path):
                os.makedirs(path)


def take_screenshots(url):
    # driver = get_driver()

    for device in devices:
        for resolution, size in devices[device].items():
            driver.set_window_size(size[0], size[1])
            driver.get(url)

            # Create filename with date and time
            filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.png'
            filepath = os.path.join(device, resolution, filename)

            # Save the screenshot
            driver.save_screenshot(filepath)
            print(f"Screenshot saved to {filepath}")

create_directories()
take_screenshots(url)

# Close the WebDriver
driver.quit()
