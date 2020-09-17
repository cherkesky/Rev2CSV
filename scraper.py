from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from secret import pid
import time
from datetime import datetime, timedelta
import csv


pid = input("Enter PID: ")

url = f'https://search.google.com/local/reviews?placeid={pid}'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(3)
saved_reviews = []
index=0 

current_url = driver.current_url
cid = current_url.split("ludocid=")[1].split("=")[0].split("&")[0]

header = driver.find_element_by_css_selector( "div[class*='review-dialog-top']" )
business_name = header.find_element_by_xpath(".//div/div/div").text
reviewsDialog = driver.find_element_by_class_name('gws-localreviews__general-reviews-block')
divs = reviewsDialog.find_elements_by_css_selector( "div[class*='gws-localreviews__google-review']" )

print ("*********************************************************")
print (business_name)
print ("*********************************************************\n")

for div in divs:
  print ("___________________________________________")
  for aaa in div.find_elements_by_tag_name("a"):
      for a in aaa.find_elements_by_tag_name("img"):
        img_alt = a.get_attribute("alt")
        img_src = a.get_attribute("src")
        print (f'Name: {img_alt}') 
        print (f'Avatar: {img_src}') 
  href = div.find_element_by_xpath(".//a")
  reviewer_id = href.get_attribute("href").split("https://www.google.com/maps/contrib/")[1].split("?")[0]
  print (f'Id: {reviewer_id}')

  spans = div.find_elements_by_tag_name('span')
  for span in spans:
    try:
      is_it_review_span = span.get_attribute("jscontroller")
      if is_it_review_span != None:
        saved_review_text = span.text
        print (f'Review: {saved_review_text}')
    except: pass

  stars_block = div.find_element_by_tag_name('g-review-stars')
  stars_span = stars_block.find_element_by_xpath(".//span")
  stars = stars_span.get_attribute("aria-label").split(".")[0].split(" ")[1]
  print (f'Stars: {stars}')

  index += 1
  str_review_date =  str(datetime.now()-timedelta(days=index)).split(".")[0]
  stamp_review_date = datetime.timestamp(datetime.now()-timedelta(days=index))
  saved_single_review = {}
  saved_single_review['id'] = index
  saved_single_review['pageid'] = pid
  saved_single_review['pagename'] = business_name
  saved_single_review['created_time'] = str_review_date
  saved_single_review['created_time_stamp'] = stamp_review_date
  saved_single_review['reviewer_name'] = img_alt
  saved_single_review['reviewer_id'] = reviewer_id
  saved_single_review['rating'] = stars
  saved_single_review['review_text'] = saved_review_text
  saved_single_review['hide'] = ''
  saved_single_review['review_length'] = str(len(saved_review_text.split()))
  saved_single_review['type'] = 'Google'
  saved_single_review['userpic'] = img_src
  saved_single_review['from_url'] = f'https://maps.google.com/?cid={cid}'
  saved_single_review['recommendation_type'] = ''
  saved_single_review['userpiclocal'] = ''
  saved_single_review['reviewer_email'] = ''
  saved_single_review['company_name'] = ''
  saved_single_review['company_title'] = ''
  saved_single_review['company_url'] = ''
  saved_single_review['review_length_char'] = str(len(saved_review_text))
  saved_single_review['userpic_small'] = ''
  saved_single_review['from_name'] = ''
  saved_single_review['from_logo'] = ''
  saved_single_review['from_url_review'] = ''
  saved_single_review['review_title'] = ''
  saved_single_review['categories'] = ''
  saved_single_review['posts'] = ''
  saved_single_review['consent'] = ''
  saved_single_review['hidestars'] = ''
  saved_single_review['miscpic'] = ''
  saved_single_review['location'] = ''
  saved_single_review['verified_order'] = ''
  saved_single_review['language_code'] = ''
  saved_single_review['unique_id'] = ''
  saved_single_review['meta_data'] = ''
  saved_single_review['owner_response'] = ''
  saved_single_review['sort_weight'] = '0'
  saved_single_review['tags'] = ''
  saved_reviews.append(saved_single_review)

with open('reviewdata.csv', mode='w') as csv_file:
  fieldnames = ['id','pageid','pagename','created_time','created_time_stamp','reviewer_name','reviewer_id','rating','review_text'
  ,'hide','review_length','type','userpic','from_url','recommendation_type','userpiclocal','reviewer_email',
  'company_name','company_title','company_url','review_length_char','userpic_small','from_name','from_logo',
  'from_url_review','review_title','categories','posts','consent','hidestars','miscpic','location','verified_order',
  'language_code','unique_id','meta_data','owner_response','sort_weight','tags']
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
