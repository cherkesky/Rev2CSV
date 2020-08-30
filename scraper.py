from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from secret import pid
import time


url = f'https://search.google.com/local/reviews?placeid={pid}'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(3)
# reviewsDialog = driver.find_element_by_class_name('review-dialog-list')

reviewsDialog = driver.find_element_by_class_name('gws-localreviews__general-reviews-block')

# spans = reviewsDialog.find_elements_by_tag_name('span')
# for span in spans:
#     print(span.text)

print (f'REVIEWS:\n', reviewsDialog.text)
driver.quit()


# div:  classname - "gws-localreviews__general-reviews-block" # Block
#     + div:  #Review X 10
#         <a>:  alt=<First Last> src=<link to user image>
#         div: #Review
#             div: #name
#             div: # reviewer # reviews
#             div: # review
#                 div: # stars
#                 div: # review
#                     span: THE ACTUAL REVIEW TEXT
#                 div: 
#         div: #Like
#         div: #Response
#    + div...
#    + div...
