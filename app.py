from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

print("Test Execution Started")

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

# Create a remote WebDriver instance connected to the Docker container's Selenium Grid
driver = webdriver.Remote(
    command_executor='http://selenium-grid:4444/wd/hub',
    options=options
)


driver.maximize_window()  # Maximize the window
time.sleep(5)

# Target URL
url = "https://www.bbc.com/news/articles/cwy4yd091dgo"
driver.get(url)

# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h1"))
)

# Parse the page with BeautifulSoup using lxml
soup = BeautifulSoup(driver.page_source, "lxml")
headings = soup.find_all('h1')

# Print the headings
for heading in headings:
    print(heading.text)

# Close the browser
driver.quit()

print("Test Execution Successfully Completed!")
