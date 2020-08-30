from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

pid = "ChIJyyWQEihvZIgRQj3iFSip-F8"
url = f'https://search.google.com/local/reviews?placeid={pid}'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(5)
content = driver.find_element_by_class_name('review-dialog-list')
print (content)