from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Edge()

driver.maximize_window()

driver.get("https:/www.youtube.com")

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)

search_box.send_keys("Priyanka Arul Mohan")
search_box.send_keys(Keys.ENTER)

video = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "video-title"))
)

video.click()

time.sleep(5)

duration = driver.execute_script(
    "return document.querySelector('video').duration"
)

print("Duration in seconds:", duration)

time.sleep(duration)


driver.quit()

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge()
driver.get("https://coolors.co/")

time.sleep(3)  # wait for page to load

actions = ActionChains(driver)
actions.send_keys(Keys.SPACE).perform()

time.sleep(5)
"""

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.SPACE)
"""