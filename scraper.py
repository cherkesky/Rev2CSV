from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from secret import pid
import time
import csv


url = f'https://search.google.com/local/reviews?placeid={pid}'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(3)
saved_reviews = []
index=0 

reviewsDialog = driver.find_element_by_class_name('gws-localreviews__general-reviews-block')
divs = reviewsDialog.find_elements_by_css_selector( "div[class*='gws-localreviews__google-review']" )

for div in divs:
  print ("___________________________________________")
  for aaa in div.find_elements_by_tag_name("a"):
      for a in aaa.find_elements_by_tag_name("img"):
        img_alt = a.get_attribute("alt")
        img_src = a.get_attribute("src")
        print (f'Name: {img_alt}') 
        print (f'Avatar: {img_src}') 
  spans = div.find_elements_by_tag_name('span')
  for span in spans:
    try:
      is_it_review_span = span.get_attribute("jscontroller")
      if is_it_review_span != None:
        saved_review_text = span.text
        print (f'Review: {saved_review_text}')
    except: pass
  
  index += 1
  saved_single_review = {}
  saved_single_review['id'] = index
  saved_single_review['name'] = img_alt
  saved_single_review['pic'] = img_src
  saved_single_review['review'] = saved_review_text
  saved_reviews.append(saved_single_review)
  # print ("REVIEW DICT", saved_single_review)

with open('TEST.csv', mode='w') as csv_file:
  fieldnames = ['id', 'name', 'pic', 'review']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  for review in saved_reviews:
   writer.writerow(review)

driver.quit()


# div:  classname - "gws-localreviews__general-reviews-block" # Block
#     + div:  #Review X 10
#         <a>:  
#             <img> alt=<First Last> src=<link to user image>
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
