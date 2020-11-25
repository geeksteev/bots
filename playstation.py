from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())
ps5_url = 'https://www.walmart.com/ip/PlayStation-5-Console/363472942'
ps4_url = 'https://www.walmart.com/ip/Sony-PlayStation-4-1TB-Slim-Gaming-Console/101507200'
class_id = 'prod-product-cta-add-to-cart'


browser.get(ps5_url)
browser.find_element_by_class_name(class_id).click()
